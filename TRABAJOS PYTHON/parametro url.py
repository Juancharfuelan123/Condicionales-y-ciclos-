def parametro(url):
    i = 0
    while i < len(url) and url[i] != '?':
        i += 1
    i += 1 
    valor1 = ""
    valor2 = ""
    while i < len(url) and url[i] != '=':
        i += 1
    i += 1  
    while i < len(url) and url[i] != '&':
        valor1 += url[i]
        i += 1
    i += 1  
    while i < len(url) and url[i] != '=':
        i += 1
    i += 1  
    while i < len(url):
        valor2 += url[i]
        i += 1

    
    print(valor1, valor2)


url = "https://retosdeprogramacion.com?year=2023&challenge=0"
parametro(url)
