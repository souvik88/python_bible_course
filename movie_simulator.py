# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:27:11 2018

@author: Souvik
"""

movies = {
        "Finding Dory":[3,5],
          "Bourne":[18,5],
          "Tarzan":[15,5],
          "Ghost Busters":[12,5]
          }

while True:
    choice = input("What movie would you like to watch?: ").strip().title()
    if choice in movies:
        age = int(input("How old are you?: ").strip())
        
        
        # check user age
        if age >= movies[choice][0]:
            
            # check enough seats
            if movies[choice][1] > 0:
                print("Enjoy movie")
                movies[choice][1] = movies[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
                break
                
        else:
            print("You are too young to watch that movie")
            break
    else:
        print("We don't have that movie")
        break