#!/usr/bin/env python

import time
import os
import pyotp
from jinja2 import Template
import ConfigParser

def seq(original, code):
    sequence = []
    for idx, x in enumerate(original):
        sequence.append(int(str(code)[idx % len(code)]) + x)

    return sequence

def generate_2fa_conf(config):
    content = open('/etc/knockd.conf.j2', 'r').read()
    template = Template(content)

    sequence = config.get('conf', 'sequence').split(',')
    sequence = [ int(x) for x in sequence ]

    secure_ports = config.get('conf', 'secure_ports').split(',')
    secure_ports = [ int(x) for x in secure_ports ]

    secret = config.get('conf', 'secret')
    hotp = pyotp.TOTP(secret)

    current = hotp.now()

    options = {
        'port_sequence': seq(sequence, current),
        'code': current,
        'secure_ports': secure_ports,
        'sequence_timeout': config.get('conf', 'sequence_timeout'),
        'command_timeout': config.get('conf', 'command_timeout'),
        'secret': secret,
    }

    return template.render(options)

def write_2fa_conf(config):
    f = open('/etc/knockd.conf','w')
    f.write(generate_2fa_conf(config))
    f.write("\n")
    f.close()
    os.system("sudo service knockd stop")
    os.system("sudo service knockd start")


config = ConfigParser.ConfigParser()
config.readfp(open('/etc/knockd.2fa.conf'))

# Cron doesn't support less than 1 minute
write_2fa_conf(config)
time.sleep(30)
write_2fa_conf(config)
