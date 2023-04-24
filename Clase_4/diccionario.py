empty_dict = {}

full_filed_dict = {
    "id": 1,
    "name": "Amanda"

}

print(empty_dict)
print(full_filed_dict)

lista_1 = ['a1', 'b2']
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ('a1', 'b2')
print(tupla_1, dict(tupla_1))

list_dimensional = [['a', '1'], ['b', '3']]
print((list_dimensional, dict(list_dimensional)))

# añadir un elemento
a = {'uno': 1, 'dos': 2}
print(a)
a['tres'] = 3
print(a)

# obtener un elemento
b = {'uno': 1, 'dos': 2, 'tres': 3}
b.get('uno')
b.get('tres')
print(b)

# eliminar
c = {'uno': 1, 'dos': 2, 'tres': 3}
print(c)
c.pop('dos')
print(c)

empty_dict_2 = dict()
print(empty_dict_2)

# full_dict = (
# genero = 'M',
# nacionalidad = 'chilena'
# )

estudiante = {
    "name": "Amanda",
    "apellido": "González",
    "edad": 13,
    "rut": "11.111.111-1"
}

print(estudiante)
for variablex in estudiante.values():
    print(variablex)

print(estudiante)
for clave, valor in estudiante.items():
    print(clave, valor)

# condicionales
# if

edad = 40
if edad > 50:
    print('Hola Don')
    print('prueba dentro de if')

print('prueba fuera de if')

edad = 80
if edad > 50:
    print('Hola Don')
    print('prueba dentro de if')

print('prueba fuera de if')


# if else

temperatura = 39
if temperatura >= 37:
    print('alerta de temperatura alta')
else:
    print('la temperatura es normal')

temperatura = 36
if temperatura >= 37:
    print('alerta de temperatura alta')
else:
    print('la temperatura es normal')

temperatura = 5
pais = 'Chile'

if temperatura < 10:
    if pais == 'Chile':
        print('hace muuuucho frío')
    else:
        print('no hace taaanto frio')

if temperatura < 10:
    print('Es altamente probable que nieve')
elif temperatura >= 10 and temperatura <= 20:
    print('Es medianamente probable que nieve')
else:
    print('No hay posibilidad de nieve')


# adivina el personaje
puede_volar = True
es_humano = True
tiene_mascara = True

if puede_volar:
    if es_humano:
        if tiene_mascara:
            print(' Es Ironman')

else:
    if not puede_volar:
        if es_humano:
            if tiene_mascara:
                print('Es Spiderman')

    else:
        if puede_volar:
            if not es_humano:
                if tiene_mascara:
                    print('Otro personaje')

# ciclos

want_exit = 'n'
while want_exit == 'n':
    print('Hola cómo estás?')
    want_exit = input('¿Quieres salir S/N?')
print('fuera del while')

want_exit = 'n'
num_questions = 0
while want_exit == 'n':
    print('Hola como estás?')
    want_exit = input('Quieres salir S/N?')
    num_questions += 1
    if num_questions == 4:
        print('Alcanzaste el máximo permitido')
        break
    print('se acabo el while')

    

    