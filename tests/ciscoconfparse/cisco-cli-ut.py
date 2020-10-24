import sys
from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse(sys.argv[1], syntax='ios')

for hostname_obj in parse.find_objects('^hostname'):
    print("hostname: " + intf_obj.text)

for intf_obj in parse.find_objects('^interface'):
    print("Interfaces: " + intf_obj.text + "\n" )