# Ansible Example Role for Testing

This is a Ansible Example Role for some Testing options for an Ansible Role

Requirements:
    None

Role Variables:
    See in the defaults Directory

Example Playbook:
- hosts: all
  gather_facts: yes
  roles:
     - ansible-role-testing-example

Tested:
 - Vagrant Ubuntu 16.04
 
License:
    MIT / BSD

Author Information:
roland@stumpner.at