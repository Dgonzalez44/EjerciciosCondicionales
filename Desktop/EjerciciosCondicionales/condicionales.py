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
Auto = int (input ("Ingresar el precio del auto y del Terreno "))
I = int (input ("Ingresar el incremento anual del Terreno: %" ))
E = int (input ( "Ingresar el decremento anual del auto: %" ))

T = (((Auto * I ) / 100)*3)/2
E = ((Auto*E)/100)*3

print (f"La mitad del incremento deL Terreno en 3 años es: {I}" )
print (f"El decremento del auto en 3 años es: $ {E}" )
if E<I:
    print("Es conveniente comprar el auto" )
else:
    print( "Es conviente comprar el Terreno")
    
  
# Ejercicio #6
Pc = int ( input ("Ingresar la cantidad de computadoras compradas" ))

t = Pc*11000
if Pc<5:
  d = t*0.10
if Pc<10:
 d = t*0.20
else:
 d = t*0.40
print (f" Total a pagar por computadoras compradas es: $ {t-d} " )
print (f"El descuento es: $ {d} " )


# Ejercicio #7
Marca = input ("Ingrese la marca ")
Valor = int ( input(" Ingrese el Valor del producto " ))

if Valor>=2000:
	valorfinal = Valor - (Valor*0.10)
else:
		valorfinal = Valor + (Valor*0.16)
if (Marca == "Nosy"):
		valorfinal = valorfinal-(Valor*0.05)
print (f"El Valor total del Producto es: $ {valorfinal} " )


# Ejercicio #8
Piezas = int (input ( "Ingrese Numero De Piezas" ))
Valor = int ( input ("Ingrese valor Por Pieza" ))

t = Piezas * Valor
if t>500000:
		i = t*0.55
		d = t*0.30
		cre = t*0.15
else:
		i = t*0.70
		d = 0
		cre = t*0.30
	   
print (f" Total a Invertir: $ {i} " )
print (f" Total a  Prestamo: $ {d} " )
print (f" Total a  Credito: $ {cre}" )
print (f"Interes: $ {i} " )


# Ejercicio #9
A = float (input ("Ingrese Primer número " ))
B = float (input ("Ingrese Segundo número " ))	
if  A == B:
    R = ( A * B )
    print (f"El resultado es : {R} " )
elif A > B:
    R = (A - B)
    print (f"El resultado es : {R} " )
elif B > A:
    R = (A + B)
    print (f"El resultado es : {R} " )
    
    
  # Ejercicio #10
Num = int ( input ("Ingrese el primer numero" ))
Num2 = int (input ("Ingrese el segundo numero" ))
Num3 = int (input ("Ingrese el tercer numero" ))

if Num>Num2 and Num>Num3:
		r = Num
	
if Num2>Num and Num2>Num3:
			r = Num2
else:
			r = Num3
print (f"El numero mayor es:  {r} ")  