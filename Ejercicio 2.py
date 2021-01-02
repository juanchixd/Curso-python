#Pedir al usuario que ingrese el precio de un producto,
#devolver el costo del iva de ese producto (21%) y en otro renglon,
#devolver el valor total del producto incluido el iva

price = float(input("Ingrese el precio del producto\n"))
iva = price*0.21
tot = price*1.21
print("El costo del iva es: %.2f" % iva)
print("El valor total del producto incluido el iva es: %.2f" % tot)