'''
    ┌─────────────────────────────┐
    │ Developed by ladopixel      │
    │ mobilERG for Arduino        │
    └─────────────────────────────┘

    https://github.com/ladopixel/mobilERG

    This Python code listens to the serial port and 
    sends via ergpy the amount of 0.1 ERG to a wallet if the calling number is correct.

    Remember that you have to configure the variables:
    · serial_port [your data]
    · user_call [your data]
    · wallet_mnemonic [your data]
    · node_url [optional]
    · send_erg [optional]
    · send_erg_wallet [optional] :)

    ergpy https://github.com/mgpai22/ergpy
'''

import hashlib
import os
import serial
from platform import node
from ergpy import helper_functions, appkit


# You must configure where your board is configured
serial_port = serial.Serial('/dev/cu.usbserial-1410', 9600)
# User phone number that is good for us. Of the user that we do trust.
user_call = 'your_number'


# Configuration for the node and the seed phrase.
node_url: str = 'http://159.65.11.55:9053/'
ergo = appkit.ErgoAppKit(node_url=node_url)
wallet_mnemonic = ''


try:
    while True:
        '''
            I decode and read the information that arrives serially, 
            if at any time it coincides with the good phone number I send the ERG.
        '''
        line = serial_port.readline()
        decoded_line = line.decode('utf-8')
        found = decoded_line.find(user_call)

        # Send 0.01 ERG to ladopixel wallet :) 9hapMiKfiFhDpxBH21rp6GKCAfNwh9BREnn1VMU4P7dAufbaTps
        if found != -1:
            send_erg = 0.01
            send_erg_wallet = '9hapMiKfiFhDpxBH21rp6GKCAfNwh9BREnn1VMU4P7dAufbaTps'
            amount = [send_erg]
            receiver_addresses = [send_erg_wallet]
            try:
                print('Transaction ↓')
                print(helper_functions.simple_send(ergo=ergo, amount=amount, wallet_mnemonic=wallet_mnemonic, receiver_addresses=receiver_addresses))
                print(f'Send 0.01 to {send_erg_wallet}')
                break
            except:
                print('ERROR Transaction!')
        
except KeyboardInterrupt:
    serial_port.close()
