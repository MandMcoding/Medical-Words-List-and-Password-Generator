#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:53:30 2023

@author: m&m
"""

import random as r

#Input
print('Welcome to Medical Password Generator')
type = input('Would you like to include medical words, or pharmaceutical drugs, or both? (medical/drugs/both) ').lowercase()
length = int(input('How many words is the password? '))

#Turning the txt file into a list (in order to pick a random word)
file = 'medical_words_list.txt' if type == 'medical' else 'prescription_pharmaceutical_drugs_medications_list.txt' if type == 'drugs' else None
med_words_list = []
if file != None:
    with open(file, 'r') as med_words:
        for word in med_words:
            med_words_list.append(word)
elif type == 'both':
    with open('medical_words_list.txt') as f1, open('prescription_pharmaceutical_drugs_medications_list.txt') as f2:
        for file in (f1, f2):
            for word in file:
                med_words_list.append(word.strip())

password = ''
#Making the password by repeadily picking random medical words
for i in range(length):
    rand_index = r.randint(1,2053)
    password += med_words_list[rand_index].capitalize()

#output
print(password)
