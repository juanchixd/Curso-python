lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista1.append(9)
print(lista1)

var1 = lista1.count(2)
print(var1)

lista2 = [10,11,12]
lista1.extend(lista2)
print(lista1)

var1 = lista1.index(5)
print(var1)

var1 = lista1.insert(5, 7)
print(lista1)

lista1.pop(5)
print(lista1)

lista1.remove(8)
print(lista1)

lista1.reverse()
print(lista1)

lista1.sort(reverse=True)
print(lista1)