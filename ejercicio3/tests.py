def multiplicar(user_numero):
    numeros = range(1, 11)
    try:
        print(f"Tabla del {user_numero}")
        for i in numeros:
            multiplicacion = user_numero * i
            print(f"{user_numero} x {i} = {multiplicacion}")

    except ValueError as e:
        print(f"Valor incorrecto, introduce un numero del 1 al 10.")
        print(e)
    except Exception as e:
        print(f"Error: {e}")

user_numero = int(input("Numero: "))
multiplicar(user_numero)



