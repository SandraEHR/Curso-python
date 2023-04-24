a = 1
b = 1

while a > 0 and a < 11:
    while b > 0 and b < 11:

        print(a, '*', b, 'es igual a: ', a * b)
        
        b += 1; 
        
        if(b == 11): print("----------"); a += 1; b = 1
        break






