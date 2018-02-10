# Ansible : Playbook Nginx
The aim of this project is to deploy a simple Nginx instance on Vagrant with a simple example website project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to run this Ansible playbook :

* [Vagrant](https://www.vagrantup.com/docs/installation/) must be installed on your computer
* Update the Vagrant file based on your computer (CPU, memory), if needed
* You must have download the ubuntu Xenial64 vagrant box :

```
vagrant box add https://app.vagrantup.com/ubuntu/boxes/xenial64
```

### Usage

A good point with Vagrant is that you can create, update and destroy all architecture easily with some commands.

Be aware that you need to be in the Vagrant directory to be able to run the commands.

#### Build Environment

Vagrant needs to init the project to run and build it :

```
vagrant up
```

After build, you can check which virtual machine Vagrant has created :

```
vagrant status
```

If all run like it is expected, you should see something like this :

```
$ vagrant status

Current machine states:

nginx01                   running (virtualbox)
```

#### Deployment

##### Over HTTP

To deploy the Nginx instance over HTTP, you just have to run the Ansible playbook nginx_http.yml with this command :

```
ansible-playbook nginx_http.yml
```

If all run like it is expected, you should access the simple website example : http://10.0.0.31/

##### Over HTTPS

To deploy the project over HTTPS, you must :

* provide SSL Certificate (maybe with LetsEncrypt)
* copy it to the file folder under : etc/ssl/RANDOMNAME
* configure the variables in the playbook nginx_https.yml

After that, you could run this command to deploy the example website over HTTPS :

```
ansible-playbook nginx_https.yml
```

If all run like it is expected, you should access the simple website example : https://10.0.0.31/

#### Destroy

To destroy on what Vagrant has created, just run this command :

```
vagrant destroy
```

## Author

Member of Wikitops : https://www.wikitops.io/
