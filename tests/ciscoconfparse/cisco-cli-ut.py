#!/usr/bin/env python

import sys
import argparse
from ciscoconfparse import CiscoConfParse


def test_hostname():
    for hostname_obj in parse.find_objects('^hostname'):
        print("hostname: " + hostname_obj.text)

def test_interfaces():
    for intf_obj in parse.find_objects('^interface'):
        print("Interfaces: " + intf_obj.text + "\n" )

def start():
script, input_file = argv
global parse
global test_total

parse = CiscoConfParse(input_file, syntax='ios')

test_hostname()
test_interfaces()


def main():
args = sys.argv[1:]
if len(args) == 1:
    start()

if __name__ = "__main__":
main()
