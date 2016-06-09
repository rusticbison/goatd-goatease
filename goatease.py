#!/usr/bin/python
#Prerequisites: 
#pip install requests
#pip install pyqrcode

import requests
import json
import pyqrcode

#Author: Justin Smith
#Date: April 27, 2016
#Description: Simple interface for working with GoatD after it has been configured

#Modified: April 28, 2016 
#Reason: Added the ability to see fees for a unit

balance="balance"
units="units"
transfers="transfers/"
fees_unitID="fees?unitID="
fees_amount="&amount="
url=('http://127.0.0.1:2360/v1.0/')

while True:
    menu=raw_input("Press 'a' to see your wallet address and generate a QR code.\nPress 'b' to see your balance.\nPress 'u' to see units available on the Notary.\nPress 's' to see the status of a pending transfer.\nPress 'n' to create a new transfer.'\nPress 'f' to see the fees for a particular unit.\nTo quit, press 'q'.\n\n")

    if menu=="b":
        r = requests.get(url + balance)
        print(r.text)
    elif menu=="a":
        r = requests.get(url + "nym-id")
        url = pyqrcode.create(r.text)
	url.svg(r.text, scale=4)
	print(url.terminal(quiet_zone=1))
	print(r.text)
    elif menu=="u":
        r = requests.get(url+units)
        print(r.text)
    elif menu=="q":
        exit(0)
    elif menu=="s":
        how_many_to_see=raw_input("Which transfer would you like to see? Enter your transfer's history number.\n")
        r = requests.get(url+transfers+how_many_to_see)
        print(r.text)
        raw_input("\n\nPress enter to continue.")
    elif menu=="n":
        unit_type=raw_input("What type of units do you want to send?\nFor Bitcoin use 432jiLUkzDwG8PqyFxiWfxMq1ijL69R3VyUUHq6o6tnv\n\n")
        unit_quantity=raw_input("How many units do you want to send?\n")
        receiver=raw_input("Who do you want to send funds to? Enter their Nym ID\n")
        payload = {receiver:{unit_type:unit_quantity}}
        r = requests.post(url + transfers, json=payload)
        print(r.text)
    elif menu=="f":
        unit_type=raw_input("Which unit would you like to see the fees for?\n\n")
        unit_quantity=raw_input("How much money are you planning to transfer?\n\n")
        r = requests.get(url + fees_unitID + unit_type + fees_amount + unit_quantity)
        #"fees?unitID=ffeoiafoieoeifiafoie&amount=10"
        print(r.text)
    else:
        print("Invalid response.")

raw_input("\n\nPress the enter key to exit.")
