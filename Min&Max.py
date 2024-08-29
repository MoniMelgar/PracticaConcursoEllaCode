# Se darán N enteros y M consultas. Las consultas trabajan sobre un arreglo S de N enteros
# Pueden ser:
# C i j: Se dará un carácter C y un intervalo.
# El intervalo estará detonado por dos enterios i y j.
# Se debe imprimir el mínimo y máximo elementos del arreglo en dicho intervalo
# A i v: se dará el carácter A seguido de un indice i y un valor v
# Se debe sobreescribir el i-ésimo elemento del arreglo S con el valor v

def Consultas():
    Consulta=input("Introduzca la consulta\nUtiliza espacios para separarlos entre sí\n").split()
    print (Consulta)

NM=input("Por favor introduzca el número de enteros y el número de consultas\nUtiliza espacios para separarlos entre sí\n").split()
print(NM)
S=input("Por favor introduzca el arreglo separado.\nUtiliza espacios para separarlos entre sí\n").split()
if NM[0]!=len(S):
    X=input("El numero de enteros solicitados es diferente al dado\nPresiona cualquier tecla diferente a 1 para continuar\n")
    if(X==1): 
        sys.exit()
    else:
        Consultas()
else:
    Consultas()