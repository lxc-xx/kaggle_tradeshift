#!/usr/bin/env python

import sys

def is_float(s):
    try:
        float(s)
    except ValueError:
        return False

    return True



with open(sys.argv[1], 'r') as sample_file:
    for item in sample_file.readlines()[0].rstrip('\n').split(','):
        if not item:
            print "empty"
        elif item == "YES" or item == "NO":
            print "BIN"
        elif is_float(item):
            print "NUM"
        else:
            print "STR"
