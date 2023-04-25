words = "Esto es una cadena de texto "

for letter in words:
    print(letter)

word = ' '
for letter in words:
    if letter !=' ':
        word += letter
    else:
        print(word)
        word =' '
print(("----------"))
for letter in words:
    if letter != ' ':
        print(letter)       
    else:
        break    

print(("----------"))    
animal_list = ['Gato', 'Perro', 'Pajaro', 'Ardilla']
for animal in animal_list:
    print(animal)

print(("----------")) 
list1 = range(2,3)
print(list1)
for number_in in range(1, 10):
    print(number_in)

print(("----------")) 
list1 = range(2,3)
print(list1)
for number_in in range(1, 10, 2):
    print(number_in)

print(("----------")) 
list1 = range(2,3)
print(list1)
for number_in in range(1, 20, 3):
    print(number_in)

print(("----------"))
for num_tabla in range(1, 11):
    for num_mult in range(1, 11):
        result = num_tabla * num_mult
        print(f'{num_tabla} x {num_mult} = {result}') 
    print(("----------"))       

