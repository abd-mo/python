
# coding: utf-8



name=input("enter  frist name: ")
surname=input("enter  surname: ")
number=input("enter person's number 'frist will be 0' = ")
number=int(number)
name=name.lower()
surname=surname.lower()

if 'ö'in name or surname:
    name=name.replace('ö','o')
    surname=surname.replace('ö','o')
if 'ğ'in name or surname:
    name=name.replace('ğ','g')
    surname=surname.replace('ğ','g')
if 'ü'in name or surname:
    name=name.replace('ü','u')
    surname=surname.replace('ü','u')
    
if 'ı'in name or surname:
    name=name.replace('1','i')
    surname=surname.replace('1','i')
    
if 'ş'in name or surname:
    name=name.replace('ş','s')
    surname=surname.replace('ş','s')
    
if 'ç'in name or surname:
    name=name.replace('ç','c')
    surname=surname.replace('ç','c')
    
if number==0:
    print(name+surname+"@posta.mu.edu.tr") 
else:
    number=number-1
    number=str(number)
    print(name+surname+number+"@posta.mu.edu.tr")





