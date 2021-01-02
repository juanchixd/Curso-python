#Pedirle al usuario que ingrese su nombre, horas trabajadas en el mes y precio por hora.
#Devolver lo que cobra esa persona
name = input("Ingrese su nombre\n")
hours = int(input("Ingrese cantidad de horas trabajadas\n"))
price = int(input("Ingrese precio por hora\n"))
print(name, "este mes vas a cobrar: ", price*hours)