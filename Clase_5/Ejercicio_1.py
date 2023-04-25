#D = 0 - 2
#C = 2.1 - 5
#B = 5.1 - 6
#A = 6.1 - 7

nota_1 = 6.5
nota_2 = 5.2
nota_3 = 5.9

promedio = (nota_1 + nota_2 + nota_3)/3
print(round(promedio, 1))

if promedio >= 0 and promedio <= 2:
    print('D')

elif promedio >= 2.1 and promedio <= 5:
    print('C')

elif promedio >= 5.1 and promedio <= 6:
    print('B')

elif promedio >= 6.1 and promedio <= 7:
    print('A')
