print("Este programa solo admite cuadrado y triangulo en sus versiones graficas")

def cuadrado(tamano):
    for k in range(tamano):
        print("*" * tamano)

def triangulo(tamano):
    for k in range(1, tamano + 1):
        print("*" * k)

# Pedimos al usuario el tamaño y la forma
tamano = int(input("Ingresa el tamano del que quieres que sea el grafico: "))
forma = input("Escribe el poligono que deseas graficar: ")

# Comparamos con los nombres en texto, no con las funciones
if forma == "cuadrado":
    cuadrado(tamano)
elif forma == "triangulo":
    triangulo(tamano)
else:
    print("No valido, solo admitimos cuadrado y triangulo")