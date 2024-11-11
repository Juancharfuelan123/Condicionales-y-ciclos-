def numeroarms(numero):
    numdigitos = len(str(numero))
    suma = 0
    for digito in str(numero):
        suma =suma + int(digito) ** numdigitos
        print(suma)
    if suma == numero:
        print(numero, "Es un numero de Armstrong.")
    else:
        print(numero, "No es un numero de Armstrong.")


numeroarms(8208)
numeroarms(403)