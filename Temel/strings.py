# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:16:41 2023

@author: meteh
"""
#substring
message = "Merhaba Dünya!"

print(message[0:4])
print(message[4:5])

newMessage = message[4:7]

print(newMessage)

#len
print(len(message))
newMessage2 = message[len(message)-1:len(message)]
print(newMessage2)

# Lower Upper
print(message.upper())
print(message.lower())

# Replace
print(message.replace("ü","u"))

print(message.replace("a","e"))

#Split
bilgi = "Metehan Ugus 26 Canakkale"
print(bilgi.split(" "))
bilgi2 = "Metehan;Ugus;26;Canakkale"
print(bilgi2.split(";"))
print(bilgi2.split(";")[3])

#Input

ad = input("Adınız?")
print(ad)

sayi1 = input("1. sayıyı giriniz")
sayi2 = input("2. sayiyi giriniz")
print("İki sayının toplamı:", int(sayi1) + int(sayi2))