# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 19:48:22 2018

@author: Souvik
"""
#get user email address
email = input("What is your email address: ").strip()
#slice out username
username = email[:email.index("@")]

#slice domain name
domain_name = email[email.index("@") + 1:]

#format message
output = "Your username is {} and your domain name is {}".format(username, domain_name)
print(output)
#display output message
