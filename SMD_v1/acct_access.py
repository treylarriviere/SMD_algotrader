# -*- coding: utf-8 -*-
"""
Account Access

Created on Sun Mar  8 22:04:49 2020

@author: Trey
"""
# Modules
import alpaca_trade_api as tradeapi
import json


# Variables list
global api
global account
global config

# Dict that the json file can iterate over.
config = {'API_KEY' : [], 'API_SECRET' : [], 'API_BASEURL' : []}


# Account Access Backend
class acct_backend():
    
    # Update Wrapper
    def update(self, x):
        self.config.update(x)
        
    #Login Method is given access to admin credentials from json file.
    def admin_login(self, config):
        # Provides the config dictionary with json file access.
        with open('config.json', 'r') as file:
            filedata = json.load(file)
            for keys in filedata:
                config['API_KEY'] = filedata["API_KEY"]
                config['API_SECRET'] = filedata["API_SECRET"]
                config['API_BASEURL'] = filedata["API_BASEURL"]
            
    # Login Method obtains credentials.
    def new_login(self, config):
         # API Account Validation
         config['API_KEY'] = input('Please input API KEY: ')
         config['API_SECRET'] = input('Please input SECRET KEY: ')
         
         # Live/Paper Account Selection
         paper_choice = input('live or paper?')
         if paper_choice == 'paper':
             config['API_BASEURL'] = "https://paper-api.alpaca.markets"
         else:
             config['API_BASEURL'] = "Leaving this blank for timebeing, not losing money yet."
             
         with open('config.json', 'w') as outfile:
             json.dump(config, outfile)
    
    # Gathers the data from the json file to add to the config dict.
    # Then takes the config data and applies it to variables.
    def login_process(self, config):
        with open('config.json') as file:
            data = json.load(file)
            for p in data:
                config['API_KEY'] = data["API_KEY"]
                config['API_SECRET'] = data["API_SECRET"]
                config['API_BASEURL'] = data["API_BASEURL"]
                
        API_KEY = config.get('API_KEY')
        API_SECRET = config.get('API_SECRET')
        API_BASEURL = config.get('API_BASEURL')
         
    # Displays the account status.
    def acct_status(self, account):
        self.account = account
        # Account Status
        if account.status == 'ACTIVE':
            print('')
            print('ACCOUNT IS ACTIVE')
            print("Welcome to ScroogeMcDuck's Vault v1")
            print('')
        else:
            print('/n')
            print('ACCOUNT IS INACTIVE // CONTACT ALPACA')
            print('/n')
