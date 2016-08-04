# GoatEase
A simple interface to send requests to a Monetas *GoatD* client. Used to manage digital contracts on the Monetas demo platform, which only uses play currencies/assets!

![goatease](https://cloud.githubusercontent.com/assets/18722686/16189424/92818aae-36da-11e6-89ef-2d8c24df690b.gif)

### Steps
This appliance uses virtual box as a vagrant provider, you can download virtual box here: https://www.virtualbox.org/wiki/Downloads 

Download the vagrant package using the link sent to you by Monetas, or [setup your own GoatD](http://goatd.monetas.net). 

Add the vagrant box to your vagrant using following command: 

```bash
$ vagrant box add goatd-1.0.93.box --name goatd-1.0.93
```

Initiate vagrant system in chosen directory

```bash
$ vagrant init
```

Open and edit your Vagrantfile, change: config.vm.box  ="base" TO config.vm.box = "goatd-1.0.93"

Now start your vagrant box

```bash
$ vagrant up
```

Login to Vagrant

```bash
$ vagrant ssh
```

Login as root

```bash
$ sudo su - 
```

Prepare the serpant

```bash
$ sudo yum install python-pip
$ pip install requests
$ pip install pyqrcode
```

Create new wallet(s)

```bash
$ newwallet
```

You'll be shown your port number, copy it. Now create your goatease.py:

```bash
$ vim goatease.py
```

Update the variable "port" with your port number. Then :wq to save and close the file. Update permissions:

```bash
$ chmod 777 goatease.py
```

Run goatease and enjoy!

```bash
$ ./goatease.py
```
If you'd like to try sending a transfer, feel free to send funds to my GoatD: Hrv9T8sQajt9oGQfE9MudSkndbaPDusGXLmessNYBAbK

Here's a list of the available play currencies:

6pkHRpVKXWNt4wY5tNXcz6kpobgg6DFCwo5o9FfYkqic - Liter Of Goat Milk With Fees

73DzxX5XgZxoRPuJwY5SrhFsEPsf7ubyeShs1QGfdzxJ - Slice Of Goat Cheese With Fees

6qYPELToPoAwc71AovjPhC5r9t2f9E4ZUd5JcwY5Tnjy - “♦”

AZQQJwE6ET4xCDKc3g72AnvoqBcTTyF1PtWzoYJD6Miq - "♥"

EodNsm5J1mxgk8Sjq8QrhRwKdJnSN2N58XJiuhxCoJc9 - "♣"

GQtgyCzJJWuz3NJuggdYsLDuf1BfTHmEHZ4Fm7uU8RRf - "♠"

8r6xxNXoAFAbUHXhDJLFsicHkPQF8oitxHdRwg1gzoGh - Swiss Franc

BSuefomsihE9YbLxci5awRGP3CwXPmPkW5vxXnGLVLJD - Yen

HT9jb2tsYxi4zDUiGTaLWFAUpNFyiaUaBZHAJ2oCxHaB - Euro

5grZJeP3cVg7a6ren2bQUnkWvcwQ13YT2DoLvPyG98kW - Tunisian Dinar
