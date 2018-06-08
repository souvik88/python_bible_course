# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:51:30 2018

@author: Souvik
"""
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
#print(len(known_users))

while True:
    print("Hello! My name is TravisBot.")
    name = input("What is your name? ").strip().capitalize()
    if name in known_users:
        #output = "Hello {}".format(name)
        #print(output)
        #print("name recognized")
        #alternatively we can say..
        print("Hello {}! \nName Recognized".format(name))
        remove = input("Would you like to be removed from the system (y/n)? ").strip().lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print("Okay, done!)
            print(known_users)
        else:
            print("No Problem!")
        break
    else:
        #output = "Hello {}".format(name)
        #print(output)
        #print("name not recognized")
        #alternatively we can say..
        print("Hello {}! \nName not recognized. \nI don't think I have met you yet.".format(name))
        add = input("Would you like to be added to user list (y/n)? ").strip().lower()
        if add == "y":
            print(known_users)
            known_users.append(name)
            print("Okay, done!")
            print(known_users)
        else:
            print("No Problem!")
        break
