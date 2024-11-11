def eliminarcaractres (str1,str2):
    out1=""
    out2=""
    for letra in str1:
        if letra not in str2 and letra not in out1:
            out1=out1+letra 
    for letra in str2: 
        if letra not in str1 and letra not in out2:
            out2=out2+letra
    print("Caracteres presentes en str1 pero que no estan presentes en out1: ", out1 )
    print ("Caracteres presentes en str2 pero que no estan presentes en out2: ",out2 )

eliminarcaractres("juan","jose")  