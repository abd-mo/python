# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:56:09 2018

@author: abdelrahman
"""

def dizi_anahtari(myliste):
    my_liste=myliste.split('-')
    t=0
    int_liste=[]
    for i in range(len(my_liste)):
              int_liste.append(int(my_liste[i]))
              t+=int(my_liste[i])
    a=t//len(int_liste)
   # print("ortalama = ",a)
    #print(int_liste)       
    sorted_liste=[]
    while len(int_liste)!=0:
          x=min(int_liste)
          sorted_liste.append(x)
          int_liste.remove(x)
    print("dizi :",sorted_liste)
    y=(len(sorted_liste))
    
    if y%2==0:
           y=y/2
           z=y-1
           w=sorted_liste[int(y)]
           r=sorted_liste[int(z)]
           b=int((w+r)/2)
           print("anahtari: ",a*b)
    elif y%2!=0 :
          f=(y//2)
          b=sorted_liste[int(f)]
          print("anahtari: ",a*b)
string="10-3-2-5"

dizi_anahtari(string)

