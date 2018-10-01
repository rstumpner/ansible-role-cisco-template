Testing the Ansible Role with Docker (Ubuntu 16.04) and use Ansible to create the Container

Requirements:
 - Ubuntu 16.04
 - Ansible 

Simple Testing:
```bash
playbook -i inventory ansible-docker-test.yml
```

Rerun the Test:
```bash
vagrant provision
```

Checking the Test Environment:
```bash
vagrant ssh
```
