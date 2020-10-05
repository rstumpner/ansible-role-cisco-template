import sys
from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse(sys.argv[1], syntax='ios')

for intf_obj in parse.find_objects('^hostname'):
    print("hostname: " + intf_obj.text)