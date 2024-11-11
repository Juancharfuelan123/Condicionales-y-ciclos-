def mmarcopalabras(texto):
    palabra = ""
    palabras = []
    longitudmax = 0

    for caracter in texto + " ":
        if caracter == " ":
            if palabra != "":
                palabras = palabras + [palabra]  
                if len(palabra) > longitudmax:
                    longitudmax = len(palabra)
                palabra = ""
        else:
            palabra = palabra + caracter

    print("*" * (longitudmax + 4))
    
    for palabra in palabras:
        linea = "* " + palabra  
        espaciosfalt = longitudmax - len(palabra)
        for _ in range(espaciosfalt):
            linea =linea + " "
        
        linea =linea +" *" 
        print(linea)
    

    print("*" * (longitudmax + 4))


texto = input("Ingresa tu texto: ")
mmarcopalabras(texto)