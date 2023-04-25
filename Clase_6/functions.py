def saludar(name):
    print(f'Hola {name} !!!')

saludar('Amanda')   
saludar('Matt')

def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name}!!!')

saludar_dos('Amanda', 'Gonzalez')   

def mult_texto(texto, multiplier):
    print(texto * multiplier)

mult_texto('Haru ', 3)   

def mult_texto_2(texto, multiplier = 5):
    print(texto * multiplier)

mult_texto_2('Hairy ')

def varietal(param_1, param_2, *others):
    print(param_1)
    print(param_2)
    print(others)

varietal('1A', '2B', 0)    

def varietal_2(param_1, param_2, **others):
    print(param_1)
    print(param_2)
    print(others)

varietal_2('1A', '2B', id = 0, name = 'Amanda')