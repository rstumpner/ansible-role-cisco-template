# Ansible Role Template for Cisco Configuration

This is a Ansible Template Role for generating Cisco Configuration and Tests itself with a CI/CD Pipeline that is contained in the Repository.So it can be used as a starting point for a new ansible role or to test some Jinja2 templates.

## Requirements:
   * Ansible 2.4+
   * python 3

## Installation:

For the first steps there is no Installation needed just clone it to your Gitlab ( https://gitlab.com ) repository and the Gitlab Runner should work.
If you want to do some test on your local machine install a Gitlab Runner there or Install Ansible (pip install ansible) and Copy & Paste the CI/CD Stages from the gitlab-ci.yml file.


## Using this Role:
Drive to Ansible Role Directory:
    - git clone https://gitlab.com/rstumpner/ansible-role-cisco-template.git

Activate this Role in a Playbook:

Example:
```YAML
- hosts: all
  geather_facts: no
  roles:
     - ansible-role-cisco-template
```
For some example configurations have a look at the main.yml in the folder defaults (https://gitlab.com/rstumpner/ansible-role-cisco-template/-/blob/master/defaults/main.yml) in this repository.

## Features:
- Hostname Configuration
- Interface L2 and L3 Configuration
- VRF Configuration

## CI/CD Stages
A short overview of the implemented Stages in the CI/CD Pipeline.

#### Validate

There should be the tasks to validate the imput sources YAML files for example. Actually its a simple Ansible syntaxcheck.

#### Build
All Tasks for building the configurations (cli/netconf/restconf) will be executed and saved as artifact.

Ansible tags: 
- build
- build-cli
- build-netconf
- build-restconf

#### Test
All Tasks for Testing the configuration or the devices are placed here . Also some pre deployment tasks could be done here like a simple configuration snapshot of the device.

Ansible Tags:
- bak
- diff
- tests

#### deploy
The deployment of the configuration will be in this stage. 

Ansible Tags:
- deploy-cli
- deploy-oam
- deploy 

## Tested:
 - Cisco IOS
 - Cisco IOS-XE

## Known Issues
Just have a look at this Repository.

https://gitlab.com/rstumpner/ansible-role-cisco-template/-/issues

## How to Contribute
Just open up an issue or get in contact via email. Actually it is under havy development and there are many ideas to contribute to this project. 

## License:
    MIT / BSD

## Author Information:
roland@stumpner.at