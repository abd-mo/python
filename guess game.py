# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
print("****welcome to guess game****")
print()
print("****you have 10 times to try****")

t=0
x='y'
while x=='y':
    rand = random.randrange(1, 1001)
    print(rand)
    a=input("enter your begining: ")
    print()
    a=int(a)
    while(1):
            t+=1
            
            if a==rand:
                print("cogratulation you have won")
                print()
                break
            elif t==10:
                print("<<<<<<<   opps,your time is ran out   >>>>>>>")
                print()
                break
            elif a>rand:
                a=int(input("your number is high: "))
                print()
             
            elif a<rand:
                a=int(input("your number is low: "))
                print()
    x=input("do you want to play again !? [y] or [N]: ")
    t=0
    if x=='Y'or 'y':
        continue
    else :break
        
   
