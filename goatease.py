#!/usr/bin/python
#Prerequisites:
#pip install requests
#pip install pyqrcode

import requests
import json
import pyqrcode
import random

#Author: Justin Smith
#Date: April 27, 2016
#Description: Simple interface for working with GoatD after it has been configured

#Modified: April 28, 2016
#Reason: Added the ability to see fees for a unit

my_nym= "Hrv9T8sQajt9oGQfE9MudSkndbaPDusGXLmessNYBAbK"
port = "23765"
version = "/v3.0/"

balance="balance"
units="units"
transfers="transfers/"
fees_unitID="fees?unitID="
fees_amount="&amount="
url= "http://127.0.0.1:" + port + version

CHF_address = "8r6xxNXoAFAbUHXhDJLFsicHkPQF8oitxHdRwg1gzoGh"
Diamonds_address = "6qYPELToPoAwc71AovjPhC5r9t2f9E4ZUd5JcwY5Tnjy"

while True:
    menu=raw_input("Press 'a' for your wallet address QR code.\nPress 'b' to see your balance.\nPress 'l' to get funds.\nPress 'u' to see units available on the Notary.\nPress 'n' to create a new transfer.'\nPress 'f' to see the fees for a unit type.\nTo quit, press 'q'.\n\n")

    if menu=="b":
        wallet_response = requests.get(url + balance)
        print(wallet_response.text)
    elif menu=="a":
        r = requests.get(url + "nym-id")
        url = pyqrcode.create(r.text)
	url.svg(r.text, scale=4)
	print(url.terminal(quiet_zone=1))
	print(r.text)
    elif menu=="u":
        r = requests.get(url+units)
        print(r.text)
        #
        #
    elif menu=="n":
        #amount=raw_input("How many Diamonds do you want to send?\n")
        #Send my phone some funds.
        unit_type=raw_input("Enter the number of the unit type you would like to send, or enter any other character to return to the main menu.\nPlease note: the only fully interoperable units right now are the playing card currencies.\n\n(1) CHF ISO4217\n(2) EUR ISO4217\n(3) JPY ISO4217\n(4) TND ISO4217\n(5) Hearts\n(6) Diamonds\n(7) Spades\n(8) Clubs\n(9) Slice Of Goat Cheese With Fees\n(10) Liter Of Goat Milk With Fees\n\n")
        amount = raw_input("Enter the amount of funds to send. Make sure you have enough, there's no error handling available!\n")
        receiver_nym=raw_input("Who do you want to send funds to? Enter their Nym ID\n")
        #
        #this code works. Leave it for testing.
        #data = '{"'BiqwM9USRHeqtXc3obukNfiTyvwF4NozrVRWL5yUzAGy'":{"6qYPELToPoAwc71AovjPhC5r9t2f9E4ZUd5JcwY5Tnjy":100}}' #receiver nym:unit to send:amount
        #requests.post('http://127.0.0.1:23765/v3.0/transfers', data=data)

        if unit_type == "5":
            data = '{ "'+ receiver_nym +'": {"AZQQJwE6ET4xCDKc3g72AnvoqBcTTyF1PtWzoYJD6Miq": '+ str(amount) +'}}' #Hearts
            requests.post(url + 'transfers', data=data)
            print("Transfer sent!\n\n")
        elif unit_type == "6":
            data = '{ "'+ receiver_nym +'": {"6qYPELToPoAwc71AovjPhC5r9t2f9E4ZUd5JcwY5Tnjy": '+ str(amount) +'}}' #Diamonds
            requests.post(url + 'transfers', data=data)
            print("Transfer sent!\n\n")
        elif unit_type == "7":
            data = '{ "'+ receiver_nym +'": {"GQtgyCzJJWuz3NJuggdYsLDuf1BfTHmEHZ4Fm7uU8RRf": '+ str(amount) +'}}' #Spades
            requests.post(url + 'transfers', data=data)
            print("Transfer sent!\n\n")
        elif unit_type == "8":
            data = '{ "'+ receiver_nym +'": {"EodNsm5J1mxgk8Sjq8QrhRwKdJnSN2N58XJiuhxCoJc9": '+ str(amount) +'}}' #Clubs
            requests.post(url + 'transfers', data=data)
            print("Transfer sent!\n\n")
        else:
            print("Let's go back to the main menu.\n")
        #r = requests.post(url+'/transfers?feesType=$fixedOutput', data=data)
        #print("Please check your balance and confirm the transfer with the recipient.")
        #
        #
    elif menu=="f":
        unit_type=raw_input("Which unit would you like to see the fees for?\n\n")
        unit_quantity=raw_input("How much money are you planning to transfer?\n\n")
        r = requests.get(url + fees_unitID + unit_type + fees_amount + unit_quantity)
        #"fees?unitID=ffeoiafoieoeifiafoie&amount=10"
        print(r.text)
    elif menu=="l":
        amount = random.randint(100,1000)
        unit_type=raw_input("Enter the number of the unit type you would like to receive, or enter any other character to return to the main menu.\n\n(1) CHF ISO4217\n(2) EUR ISO4217\n(3) JPY ISO4217\n(4) TND ISO4217\n(5) Hearts\n(6) Diamonds\n(7) Spades\n(8) Clubs\n(9) Slice Of Goat Cheese With Fees\n(10) Liter Of Goat Milk With Fees\n\n")
        if unit_type == "1":
            data = '{ "'+ my_nym +'": {"8r6xxNXoAFAbUHXhDJLFsicHkPQF8oitxHdRwg1gzoGh": '+ str(amount) +'}}' #Swiss Franc
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            wallet_response = requests.get(url + balance)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "2":
            data = '{ "'+ my_nym +'": {"HT9jb2tsYxi4zDUiGTaLWFAUpNFyiaUaBZHAJ2oCxHaB": '+ str(amount) +'}}' #Euro
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "3":
            data = '{ "'+ my_nym +'": {"BSuefomsihE9YbLxci5awRGP3CwXPmPkW5vxXnGLVLJD": '+ str(amount) +'}}' #Yen
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "4":
            data = '{ "'+ my_nym +'": {"5grZJeP3cVg7a6ren2bQUnkWvcwQ13YT2DoLvPyG98kW": '+ str(amount) +'}}' #TND
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "5":
            data = '{ "'+ my_nym +'": {"AZQQJwE6ET4xCDKc3g72AnvoqBcTTyF1PtWzoYJD6Miq": '+ str(amount) +'}}' #Hearts
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "6":
            data = '{ "'+ my_nym +'": {"6qYPELToPoAwc71AovjPhC5r9t2f9E4ZUd5JcwY5Tnjy": '+ str(amount) +'}}' #Diamonds
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "7":
            data = '{ "'+ my_nym +'": {"GQtgyCzJJWuz3NJuggdYsLDuf1BfTHmEHZ4Fm7uU8RRf": '+ str(amount) +'}}' #Spades
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "8":
            data = '{ "'+ my_nym +'": {"EodNsm5J1mxgk8Sjq8QrhRwKdJnSN2N58XJiuhxCoJc9": '+ str(amount) +'}}' #Clubs
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "9":
            data = '{ "'+ my_nym +'": {"73DzxX5XgZxoRPuJwY5SrhFsEPsf7ubyeShs1QGfdzxJ": '+ str(amount) +'}}' #Slice Of Goat Cheese With Fees
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        elif unit_type == "10":
            data = '{ "'+ my_nym +'": {"6pkHRpVKXWNt4wY5tNXcz6kpobgg6DFCwo5o9FfYkqic": '+ str(amount) +'}}' #Liter Of Goat Milk With Fees
            requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
            print("Please check your balance, you should have received some units.\n")
        else:
            print("Let's go back to the main menu.\n")
        # faucet_address = "http://platformdemo-faucet.monetas.io/v3.0/transfers"
        # payload_string = {'Hrv9T8sQajt9oGQfE9MudSkndbaPDusGXLmessNYBAbK':{'5grZJeP3cVg7a6ren2bQUnkWvcwQ13YT2DoLvPyG98kW':1011}}
        # my_nym = '9NCL5DYxLLNq1U2AgMVn8u27pMvLaVBXtMy57XktDvd6'
        # faucet_unit = '5grZJeP3cVg7a6ren2bQUnkWvcwQ13YT2DoLvPyG98kW'
        # faucet_amount = 1011
        # payload = {my_nym:{faucet_unit:faucet_amount}}
        # f = requests.post(faucet_address, json=payload_string)
        # f = requests.post(faucet_address, json=payload)
        #
        # This stuff below works:
        # data = '{ "Hrv9T8sQajt9oGQfE9MudSkndbaPDusGXLmessNYBAbK": {"6pkHRpVKXWNt4wY5tNXcz6kpobgg6DFCwo5o9FfYkqic": 10110}}'
        # requests.post('http://platformdemo-faucet.monetas.io/v3.0/transfers', data=data)
        # wallet_response = requests.get(url + balance)
        # print(wallet_response.text)
    elif menu=="q":
        exit(0)
    else:
        print("Invalid response.")

raw_input("\n\nPress the enter key to exit.")
