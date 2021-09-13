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


# Ejercicio #2
Valor = int (input (" Ingrese el valor total de la compra "))
	
Numero = int (input(" Ingrese el numero escogido " ))


if Numero >= 74:
		t = Valor * 0.20
else:
		t = Valor * 0.15
print( f"Total a pagar con descuento  incluido es: $,{Valor - t}" )
print (f"Descuento aplicado es: $ ,{t}" )


# Ejercicio #3
Valor = int (input( " Ingrese el monto a financiar" ))

Numero = int (input ( "Digite un numero:"  ))
	
if Valor > 50000:

		t = Valor*0.02
else:
		t = Valor*0.03
print (f"Interes a pagar es: $  {t} " )
print (f"Cuota total a pagar es: $ {Valor + t}")


# Ejercicio #4
Dias = int (input ("Ingresa los puntos de la fabrica de cada uno de los días"))
    
	
Ganancia = int (input ("Ingresa las ganancias de los días"))
	
if Dias > 170:
		m = Ganancia*0.05
else:
		m = 0
print (f"Promedio de puntos de la fabrica es: {Dias} " )
print (f"Ganancia  de una semana de la fabrica es: $ {Ganancia} " )
print (f"Pérdida de dinero por la revision es: $ { m } " )


# Ejercicio #5
