# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 20:50:52 2023

@author: natan
"""

time = input("quais horas são neste modelo 00:00?")

def  testeValorValido(time):
    hora = int(time[:2])
    minuto = int(time[3:])
    if len(time) != 5:
        print("Qual parte do vc tem que digitar a hora assim 12:34 vc não entendeu?")
    elif time[2] != ":":
        print("vc deve digitar : entre a hora e os minutos")
    elif minuto > 59:
        print("Digite um valor entre 00 e 59")
    else:
        printHora(hora)
    
def printHora(hora):
    if hora > 24:
        print("one day just has 24 hours, you stupid")
    elif hora > 17:
        print("Good Evening")
    elif hora > 11:
        print("Good Afternoon")
    elif hora > 5:
        print("Good Morning")
    else:
        print("Good Night")

try:
    hora = int(time[:2])
    minuto = int(time[3:])
    testeValorValido(time)
except ValueError:
    print("digite horas com números, não com caracteres")        
