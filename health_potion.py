# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:54:57 2018

@author: Souvik
"""

import random
health = 50
difficulty = 3
potion_health = int(random.randint(25, 50) / difficulty)
health = health + potion_health
print("health_potion is {} and health is {}".format(potion_health, health))