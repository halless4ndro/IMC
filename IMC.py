# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:20:23 2020

@author: Hallessandro
"""

peso=float(input("Informe o peso "))
altura=float(input("Informe altura "))
IMC=round(peso/(altura**2),2)
if IMC<16:
  print(f"IMC igual a {IMC} - Subpeso Severo")
elif IMC>=16 and IMC<20:
  print(f"IMC igual a {IMC} - Subpeso")
elif IMC>=20 and IMC<25:
  print(f"IMC igual a {IMC} - Peso Normal")
elif IMC>=25 and IMC<30:
  print(f"IMC igual a {IMC} - Sobrepeso")
elif IMC>=30 and IMC<40:
  print(f"IMC igual a {IMC} - Obeso")
else:
  print(f"IMC igual a {IMC} - Obeso Mórbido")