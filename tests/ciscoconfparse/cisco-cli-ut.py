#!/usr/bin/env python

import sys
import argparse
from ciscoconfparse import CiscoConfParse


def test_hostname():
    global tests_total
    for hostname_obj in parse.find_objects('^hostname'):
        print("Found hostname: " + hostname_obj.text)
        test_total += 1
    return;

def test_interfaces():
    global tests_total
    for intf_obj in parse.find_objects('^interface'):
        print("Interfaces: " + intf_obj.text + "\n" )
        tests_total += 1
    return;

def start():
    script, input_file = argv
    global parse
    global tests_total

    parse = CiscoConfParse(input_file, syntax='ios')

    test_hostname()
    test_interfaces()
    print("TOTAL" + tests_total + "\n")
    return;

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        start()
    return;

if __name__ == "__main__":
    main()
