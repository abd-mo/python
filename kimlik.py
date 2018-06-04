# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 11:21:53 2018

@author: abdelrahman
"""
while (1) :
    a=input("enter your id number :")
    list1=[]
    b=len(a)
    if b<9 or b>9:
        print("pleas enter 9 numbers only")
    else :break   
x=0
y=0
list2=[]
for i in a:
    list1.append(i)    
for i in range(len(list1)):
    list2.append(int(list1[i]))
for i in list2:
    if i%2==0:
        x+=i
    else:y+=i
q=y*7-x
s1= q%10
s2=(x+y+s1)%10


        

print(s1)
print(s2)
v=a+str(s1)+str(s2)
print(a+str(s1)+str(s2))

#print(y)
#print(x)
