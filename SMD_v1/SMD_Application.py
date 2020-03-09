# -*- coding: utf-8 -*-
"""

Scrooge McDuck's Vault -- Version 1 --

Created on Sun Mar  8 22:14:59 2020

@author: Trey
"""

# Module/Variable imports.
import alpaca_trade_api as tradeapi
import acct_access
import json
from acct_access import config
acct_link = acct_access.acct_backend()
api = tradeapi.rest

# A singular instance of a user.
class User_instance():

    # Admin / New Login -- combines login processes from acct_access
    def User_login():
        
        # Choice -- Admin/New User login
        print('')
        print('')
        print('If you would like to login as an admin select yes. (Y/N)')
        if input() == 'Y':
            acct_link.admin_login(acct_access.config)
        else:
            acct_link.new_login(acct_access.config)
        
        # Accesses the API as well as retrieving all account info.
        userlogin = tradeapi.REST(acct_access.config['API_KEY'], acct_access.config['API_SECRET'], acct_access.config['API_BASEURL'])
        account1 = userlogin.get_account()
        
        # Account Status
        print(acct_link.acct_status(account1))
        print(account1)
        
    # For deleting sensitive JSON file info.
    def json_del():
        open('config.json', 'w').close()

    
    
User_instance.User_login()
# Remove JSON configurations by uncommenting.
# User_instance.json_del()
    
    


