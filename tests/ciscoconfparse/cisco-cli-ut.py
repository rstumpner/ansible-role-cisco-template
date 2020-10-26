#!/usr/bin/env python

import sys
from sys import argv
import argparse
from ciscoconfparse import CiscoConfParse


def testhostname():
    tests = 0
    for hostname_obj in parse.find_objects('^hostname'):
        print("Found hostname: " + hostname_obj.text)
        tests = tests+1
    return tests  

def testinterfaces():
    tests = 0
    for intf_obj in parse.find_objects('^interface'):
        print("Interfaces: " + intf_obj.text + "\n" )
        tests += 1
    return tests

def start():
    script, input_file = argv
    global parse
    # Reading of the Cisco Config file
    parse = CiscoConfParse(input_file, syntax='ios')
    teststotal = 0
    teststotal = teststotal + testhostname()
    teststotal = teststotal + testinterfaces()
#    print(teststotal)
    print("TOTAL:" + str(teststotal) + "\n")
    

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        start()
    else:
        print("Please give me a Filename as input")

if __name__ == "__main__":
    main()