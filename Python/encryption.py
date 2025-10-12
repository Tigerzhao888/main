#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 02:02:17 2025

@author: zhaozhihao
"""

info={
      'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
      'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
      't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, ',':27, '.':28
      }

def encrypt_text(text):
    text = text.lower()               
    encrypted = []                   
    for char in text:
        if char in info:             
            encrypted.append(info[char])
            
    return encrypted



def encrypt_file():
    filename = input("Enter the name of the plaintext file ").strip()
    with open(filename, 'r') as file:
        text = file.read()
    encrypted_list = encrypt_text(text)
    encrypted_text = ""
    for item in encrypted_list:
        encrypted_text += str(item) + " "
    
    with open("encrypted.txt", 'w') as output:
        output.write(encrypted_text)
