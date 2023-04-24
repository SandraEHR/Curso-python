first_name = "Sandra"
last_name = "Huaiquinir"
print(first_name + " " + last_name)

mensaje1 = "Hola " * 3
print(mensaje1)

mensaje_2 = "Amanda"
mensaje_2 += " $"
print((mensaje_2))
mensaje_2 += " Gonzalez"
print((mensaje_2))

print(len(mensaje_2))

cadena = "Mis gatos están locos"
posicion = cadena. find("perrito")
print("perrito se encuentra en: ", posicion)
posicion = cadena.find("gatos")
print("gatos se encuentra en: ", posicion)

# buscar funciones replace y lower
cadena = "Me gusta Mac"
nueva_cadena = cadena.replace("Mac", "Window")
print(nueva_cadena)

# listas

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name: ami"}, (1, 3, 5)]
print(fullfiled_list)

second_list = list()
print(second_list)

print(list("Concurso"))

range_one = range(50)
print(list(range_one))

numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)

print(numeros[2])

nombres = ["amanda", "isabel", "emma"]
print(nombres)
nombres.remove("emma")
print(nombres)

a = 1
print(a)
b = 'Hola'
a = 3
print(a)

empty_tuple = ()
fullfiled_tuple = (1, "Hairy", 0.05)
print(empty_tuple, fullfiled_tuple)

one_tuple = ("Hairy,")
print(type(one_tuple))

list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)


# sort
# tuple_1 = (6, 3, 8, 2, 7, 9)
# tuple_1.sort()
# print(tuple_1)

lista_1 = [6, 3, 8, 2, 7, 9]
lista_1.sort()
print(lista_1)
