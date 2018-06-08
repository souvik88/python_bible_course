# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:53:57 2018

@author: Souvik
"""
# get sentence from user
# split sentence into words
# loop through words and convert to pig latin
# if starts with vowel, just add "yay"
# otherwise, move the first consonant cluster to end, and add "ay"
# stick words back together
# output the final string

original = input("Enter a sentence: ").strip().lower()


words = original.split()


new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
        
output = " ".join(new_words)
print(output)


