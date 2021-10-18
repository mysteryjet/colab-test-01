'''
Escriba un programa que solicite repetidamente al usuario números enteros hasta que el usuario ingrese 'listo'.
Una vez que se ingrese "listo", imprima el mayor y el menor de los números. 
Si el usuario ingresa algo que no sea un número válido, 
descárguelo con un try / except y envíe un mensaje apropiado e ignore el número. 
Ingrese 7, 2, bob, 10 y 4 y haga coincidir la salida a continuación.
'''
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" :
            break
        else :
            fnum = float(num)
    except:
        print("Invalid input")
    
    
    if largest is None and smallest is None :
        largest = fnum
        smallest = fnum
    elif fnum > largest :
        largest = fnum
    elif fnum < smallest :
        smallest = fnum
    
    
print("Maximum", largest)
print('Minimum', smallest)