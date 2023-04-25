multiplicando = 1
multiplicador = 1

while multiplicando > 0 and multiplicando < 11:
    while multiplicador > 0 and multiplicador < 11:

        print(multiplicando, '*', multiplicador, 'es igual a: ', multiplicando * multiplicador)
        
        multiplicador += 1; 
        
        if(multiplicador == 11): print("----------"); multiplicando += 1; multiplicador = 1
        break






