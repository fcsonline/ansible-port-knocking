#!/usr/bin/env python

import sys
import pyotp

def seq(original, code):
    sequence = []
    for idx, x in enumerate(original):
        sequence.append(int(str(code)[idx % len(code)]) + x)

    return sequence

sequence = sys.argv[1].split(',')
sequence = [ int(x) for x in sequence ]
new_sequence = seq(sequence, sys.argv[2])
new_sequence = [ str(x) for x in new_sequence ]

print(' '.join(new_sequence))
