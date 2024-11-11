def cadenainversa(cadena):
    cadenainv = ""
    itera = len(cadena) - 1
    while itera >= 0:
        cadenainv = cadenainv +cadena[itera]
        itera = itera-1
    return cadenainv


texto = input("Ingresa la cadena que sees invertir: ")
print("Tu cadena en su version  invertida es:", cadenainversa(texto))

