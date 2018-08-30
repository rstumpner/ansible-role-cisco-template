# Ansible Role build-config-cisco for the Netdeploy Pipeline


Cisco Config Templates in Jinja2 to Generate Files for Cisco Switches to paste the Config.

Requirements:
    None

Role Variables:
    See in the Default Directory

Example Playbook:
- hosts: network
  gather_facts: no
  roles:
     - build-config-cisco-ios

Tested:
 - Cisco IOS-XE
 - Cisco NX-OS

License:
    MIT / BSD

Author Information:
Roland Stumpner 
