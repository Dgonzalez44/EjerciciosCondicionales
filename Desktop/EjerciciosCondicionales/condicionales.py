# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:22:26 2021

@author: doalf
"""

# Ejercicio #1
cantidad = int(input("Ingrese la cantidad de camisas compradas: " ))
v = int(input("Ingrese el valor de las camisas que compro: $"))

if cantidad >= 3:
	t = v*0.30
else:
    t = v*0.10
print(f"el total a pagar: ${v-t}")
print(f"el descuento aplicado es: ${t}")

