name = input("Whats your name?")
print("Bienvenido", name)

num1 = int(input("Enter a number"))
num2 = int(input("Other number"))
print("Sum=", num1+num2)

price = int(input("Tell me the price of the product"))
print("The product is worth", price)
print("Hello", name, "the product is worth", price)

print("Hello %s the product is worth %d" % (name, price))