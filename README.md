# GoatEase
A simple interface to send requests to a Monetas *GoatD* client. Used to manage digital contracts.

### Steps
This appliance uses virtual box as a vagrant provider, you can download virtual box here: https://www.virtualbox.org/wiki/Downloads 

Download the vagrant package using the link sent to you by Monetas. 

- Add the vagrant box to your vagrant using following command: 
$ vagrant box add goatd-1.0.93.box --name goatd-1.0.93

- Initiate vagrant system in chosen directory
$ vagrant init

- Open  and edit Vagrantfile, change: config.vm.box  ="base" TO config.vm.box = "goatd-1.0.93"

- Start vagrant box
$ vagrant up

- Login to Vagrant
$ vagrant ssh

- Login as root (
$ sudo su - 

- Create new wallet(s)
$ newwallet

- To check if wallets were created use ps
$ ps auxf  

- Copy goatease.py to your *GoatD* vagrant box
- Run ./goatease.py
- Enjoy!
