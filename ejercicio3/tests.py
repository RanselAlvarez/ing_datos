vocales = ["a", "e", "i", "o", "u"]


def contador_vocales(frase):
    contador = 0
    
    for i in frase:
        if i in vocales:
            contador += 1
    
    
    print(f"Hay un total de {contador} vocales.")
    
    
    
frase = input("Escribe tu frase: ")
contador_vocales(frase)