#!/usr/bin/env python

import sys
from sys import argv
import argparse
from ciscoconfparse import CiscoConfParse
from jinja2 import Template

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

def testvrf():
    tests = 0
    for vrf_obj in parse.find_objects('^vrf definition'):
        print("VRFs: " + vrf_obj.text + "\n" )
        tests += 1
    return tests

def start():
    script, input_file = argv
    global parse
    # Reading of the Cisco Config file
    parse = CiscoConfParse(input_file, syntax='ios')
    unittests = [
        {'name': 'TOTAL','testcounter': testhostname()+testinterfaces()+testvrf(),'miss': 0 ,'coverage':'100%' },
    ]

    j2_template = Template("{{ unittests.name }} {{ unittests.testcounter }} {{ unittests.miss }} {{ unittests.coverage }}")
    ut_report = j2_template.render(unittests=unittests[0])
    print(ut_report)
    

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        start()
    else:
        print("Please give me a Filename as input")

if __name__ == "__main__":
    main()