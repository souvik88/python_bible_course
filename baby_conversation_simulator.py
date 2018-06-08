# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:12:09 2018

@author: Souvik
"""
from random import choice
questions = ["Why is the sky blue?", "Why is there a face on the moon?", "Where are all the dinos?"]
question = choice(questions)
answer = input("Why is the sky blue?: ").strip().lower()

while answer != "just because":
    answer = input("Why?:").strip().lower()
print("oh.. okay")