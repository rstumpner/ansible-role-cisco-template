Testing the Ansible Role with Vagrant and Ubuntu 16.04

Requirements:
 - Virtualbox
 - Vagrant

Simple Testing:
```bash
vagrant up
```

Rerun the Test:
```bash
vagrant provision
```

Checking the Test Environment:
```bash
vagrant ssh
```

n9k3

no password strength-check
username vagrant password vagrant role network-admin

test local connect:
ssh vagrant@10.0.2.15 vrf management

ssh -l vagrant 10.0.2.15