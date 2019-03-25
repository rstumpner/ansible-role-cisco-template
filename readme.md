# Ansible Role Cisco Hostname

This is a Ansible Role for setting Hostnames on Cisco Devices.

Aufbau:
- Build Cisco Config
  - All Availiable Build Modules
    - All ansible modes
    - tags: build
  - Cisco IOS CLI
    - All ansible modes
    - tags: 
      - build
      - cli
- Testing Device Config
  - Snapshot of Device Running Config
    - All ansible modes
    - tags:
      - bak
  - Snapshot of Device state Config
    - All ansible modes
    - tags:
      - bak
  - Testing Config changes (--diff)
    - All ansible modes
    - tags:
- Deploy Device Config
  - Deploy Config with CLI
    - not ansible check-mode
    - tags:
      - oam
      - cli 

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