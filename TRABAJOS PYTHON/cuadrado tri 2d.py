print("Este programa solo admite cuadrado y triangulo en sus versiones graficas")

def dcuadrado (tamano):
    for k in range(tamano):
        print("*" * tamano )

def dtriangulo (tamano):
    for k in range(1,tamano+1):
        print("*" * k)

tamano=int(input("Ingresa el tamano del que quieres que sea el grafico: "))

forma=input("Escribe el poligono qque deseas graficar: ")

if forma== "cuadrado" :
    dcuadrado(tamano)
elif forma== "triangulo" :
    dtriangulo(tamano)    
else:
    ("No valido,solo admitimos cuadrado y triangulo")    