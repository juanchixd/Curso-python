cadena = "hello world"
result = cadena.capitalize()
print(result)

cadena = "hello world"
result = cadena.count("o")
print(result)

cadena = "hello world"
result = cadena.endswith("o")
print("Termina en o?", result)

cadena = "hello world"
result = cadena.find("z")
print("Tiene la z?", result)

cadena = "hello world"
result = cadena.isnumeric()
print(result)

cadena = "12312"
result = cadena.isnumeric()
print("es cadena numerica:", result)

cadena = "HELLO WorLD"
result = cadena.lower()
print("pasa a minuscula", result)

cadena = "hello world"
result = cadena.replace("hello", "bye")
print("reemplaza", result)

cadena = "    hello world     "
result = cadena.strip()
print("limpia espacio:", result)

cadena = "HELLO WorLD"
result = cadena.upper()
print("pasa a mayuscula:", result)

cadena = "HELLO WorLD"
result = cadena.zfill(20)
print("llena con 0 hasta 20:", result)
