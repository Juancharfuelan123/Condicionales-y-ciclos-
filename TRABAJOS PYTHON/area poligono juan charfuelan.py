print("Bienvenido/a,en este programa calcularemos el area de algunos poligonos como el triangulo,cuadrado y rectangulo")

def calculoArea (tipopoli, altura=0,base=0,lado=0):
    if tipopoli == "triangulo":
        return (base * altura)/ 2
    elif tipopoli == "cuadrado":
        return lado * lado
    elif tipopoli == "rectangulo":
        return base * altura
    else:
        return "El poligono del cual deseas calcular al area no es apto para este programa:C"
    
tipopoli=input("Ingresa tu tipo de poligono: ")

if tipopoli == "triangulo":
    base=float(input("Ingresa el valor de la base de tu triangulo: "))
    altura=float(input("Ingresa el valor de la altura de tu triangulo: "))
    area=calculoArea(tipopoli,base=base,altura=altura)
elif tipopoli == "cuadrado":
    lado=float(input("Ingresa el valor del lado de tu cuadrado: "))
    area=calculoArea(tipopoli,lado=lado)
elif tipopoli == "rectangulo":
    base=float(input("Ingresa el valor de la base de tu rectangulo: "))
    altura=float(input("Ingresa el valor de la altura de tu rectangulo: "))
    area=calculoArea(tipopoli,base=base,altura=altura)  
else:
    area="El poligono del cual deseas calcular el area no es valido para este programa"

print("El area del poligono seleccionado es igual a: ",area)