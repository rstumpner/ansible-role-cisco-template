# Ansible Role Cisco Hostname

This is a Ansible Role for setting Hostnames on Cisco Devices.

Aufbau:
- Build
- Test
    - snap
    - testing changes (--diff)

Requirements:
    None

Role Variables:
    - hostname

Using this Role:
Drive to Ansible Role Directory:
    - git clone https://fhzengitlab1.fhooe.at/P50010/cisco-hostname.git

Aktivate Role in a Playbook:

Example:
```YAML
- hosts: all
  roles:
     - cisco-hostname
```

Tested:
 - Cisco IOS
 - Cisco IOS-XE
 
License:
    MIT / BSD

Author Information:
roland@stumpner.at