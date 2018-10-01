Testing the Ansible Role with Docker (Ubuntu 16.04) and use Ansible to create the Container

Requirements:
 - Ubuntu 16.04
 - Ansible 
 - pip install docker-py
  
Simple Testing:
```bash
ansible-playbook -i hosts ansible-docker-test.yml
```

Rerun the Test:
```bash
vagrant provision
```

Checking the Test Environment:
```bash
vagrant ssh
```
