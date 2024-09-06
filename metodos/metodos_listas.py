lista = list ([1996,4,7,True])
#Nos devuelve la longitud de la lista
cadena= "hola"
resultado = len(lista)
#agregando un elemento a la lista
lista.append(28)
#agregando un elemento en una exposicion especifica
lista.insert(2,False)
#agregando varios elementos a la lista
lista.extend([2023])
#removiendo un elemento de la lista
lista.pop(0)
print(len(lista))
lista.pop(-1)
print(lista)
#eliminando un elemento de la lista por su valor
#lista.remove("Velasquez")
#ordena los elementos de la lista mientras tenga numeros y booleanos
lista.sort()
print(lista)
lista.sort(reverse=True)
#verifincando si un elemento esta en una lista
elemento_encontrado = lista.index(28)
print(elemento_encontrado)
