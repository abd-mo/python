# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:42:26 2018

@author: abdelrahman
"""

def liste_analizi(mylist):
    int_list=[]
    float_list=[]
    string_list=[]
    list_list=[]
    boolean_list=[]
    for i in range(len(mylist)):
        if isinstance(mylist[i], bool)==True:
            boolean_list.append(mylist[i])
        elif isinstance(mylist[i], int)==True:
            int_list.append(mylist[i])
        elif isinstance(mylist[i], float)==True:
              float_list.append(mylist[i])
        elif isinstance(mylist[i], list)==True:
              list_list.append(mylist[i])
        elif isinstance(mylist[i], str)==True:
              string_list.append(mylist[i])
    print("liste :",mylist,"\n")          
    print("tamsayi sayisi : ",len(int_list))
    print("ondalikli sayi sayisi : ",len(float_list))
    print("liste sayisi : ",len(list_list))
    print("boolean sayisi : ",len(boolean_list))
    print("karakter dizisi sayisi : ",len(string_list),"\n")
       
mylt=["H2O",18,0,100.0,'Bilesik',"kovalent",["hiydrogen",2],1,["oksijen",1],3,True,False,5,5.8]
liste_analizi(mylt)
print()
su=["abdelraman",["ali",5],[5.6,8],True]
liste_analizi(su)
    

    