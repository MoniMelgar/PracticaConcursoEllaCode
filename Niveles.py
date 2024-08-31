# Estrategia 1: Se multiplican los dígitos de la puntuación
# Estrategia 2 Se suman los cuadrados de los dígitos de la puntuación

def multiplicacion(lista):
    lista=[int(x) for x in lista]
    result=lista[0]
    for i in range(1, len(lista)):
        result=list[i]*result
    return [result]

def exponencial(lista):
    lista=[int(x) for x in lista]
    result=lista[0]**2
    for i in range(1, len(lista)):
        result=(list[i]**2)+result
    return [result]

def evaluación(nivel):
    A=0
    B=0
    print("nivel n°", nivel+1)
    a,b=[int(x) for x in input("Por favor ingrese el intervalo de posibles puntajes para el nivel\n").split()]
    if a==b:
        if (multiplicacion(str(i).split()))>(exponencial(str(i).split())):
            A+=1
        else:
            B+=1
    else:
        for i in range(a,b+1):
            if (multiplicacion(str(i).split()))>(exponencial(str(i).split())):
                A+=1
            else:
                B+=1
    print(A,B)

n=int(input("Ingrese el número de niveles por favor\n"))
for i in range(n):
    evaluación(i)