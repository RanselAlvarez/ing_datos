from random import randint

numero_random = randint(1, 10)
numeros_utilizados = []
numeros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("MENU")
print("Elige un numero del 1 al 10.")



try:
    while True:
        print()
        user_number = int(input("Tu numero: "))
        if user_number in numeros_utilizados:
            print(f"EL numero {user_number} ya lo utilizaste.")
            
        if user_number != numero_random:
            numeros_utilizados.append(user_number)
            if user_number in numeros_validos:
                numeros_validos.remove(user_number)
            else:
                continue
    
            print(f"Sigues con vida.")
            print(f"Te quedan estos numeros: ")
            for numero in numeros_validos:
                print(f"{numero}", end=", ")
                
        else:
            print("Perdiste, encontraste el numero maldito.")
            break
                
except Exception as e:
    print(f"Ocurrio un problema: {e}")