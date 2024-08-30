# Estrategia 1: Se multiplican los dígitos de la puntuación
# Estrategia 2 Se suman los cuadrados de los dígitos de la puntuación



n=int(input("Ingrese el número de niveles por favor"))
for i in range(n):
    a,b=[int(x) for x in input("Por favor ingrese el intervalo de posibles puntajes para el nivel ").split()]
    print (a,b)