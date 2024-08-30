# Hay 3 categorias: técnica (T), estilo (E) y presentación (P)
# Las calificaciones varian desde 0 hasta 10
def puntaje():
    punt=[int(x) for x in input("Introduzca las puntuaciones del patinador en el siguiente orden: Técnica, Estilo y Presentación\n").split()]
    if len(punt)==3 and punt[0]>=0 and punt[0]<=10 and punt[1]>=0 and punt[1]<=10 and punt[2]>=0 and punt[2]<=10:
        print("La suma total de las tres puntuaciones es: ", punt[0], " + ", punt[1], " + ", punt[2], " = ", sum(punt))
    else:
        print("Se introdujeron puntuaciones no validas, intentelo nuevamente")

x=1
while (x==1):
    puntaje()
    x=int(input("Si desea realizar una suma más de puntuaciones presione 1\n"))
print("Saliendo...")
