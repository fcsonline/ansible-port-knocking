Ansible Port Knocking
=========

Any computer connected to the Internet is inevitably targeted by malicious users and scripts
hoping to take advantage of security vulnerabilities.

Ansible Port Knocking lets you add an extra layer of security for your
infrastructure. This Ansible role enables [port knocking](https://en.wikipedia.org/wiki/Port_knocking)
feature for all specified servers.

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed in the metadata file.


Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

- **port_sequence**: array of ports that builds the knocking sequence (Example: *[24334,34534,2287]*) **Mandatory**
- **secure_ports**: array of ports to enable after a successful knocking sequence (Example: *[22]*) **Mandatory**
- **open_ports**: array of ports always available (Example: *[80, 443]*) (Default: [])
- sequence_timeout: number of seconds to be able to introduce the knocking sequence (Default: 15)
- command_timeout: number of seconds to be able to introduce a command (Default: 20)

We recommend to store the `port_sequence` variable in a secure place, like
[Ansible Vault](http://docs.ansible.com/ansible/playbooks_vault.html)

Dependencies
------------

None

Example Playbook
----------------

This is an example of role configuration:

    - hosts: servers
      roles:
         - { role: fcsonline.ansible-port-knocking, port_sequence: [24334,34534,2287], secure_ports: [22], open_ports: [80, 443] }


License
-------

BSD


Author Information
------------------

Ferran Basora <fcsonline@gmail.com>
