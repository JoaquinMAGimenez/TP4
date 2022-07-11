#ejercicio21.py

from listas import Lista


class Pelicula:
    
    def __init__(self, nombre, valoracion_del_publico, anio_de_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion_del_publico = valoracion_del_publico
        self.anio_de_estreno = anio_de_estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return self.nombre

lista_peliculas = Lista()



peliculas = [
    {'name': 'Iron Man', 'valoracion del publico': 10, 'anio de estreno':2008 , 'recaudacion':'585,8millones'},
   {'name': 'Thor', 'valoracion del publico': 9, 'anio de estreno': 2011, 'recaudacion':'449,3millones'},
   {'name': 'Aqua Man', 'valoracion del publico': 2, 'anio de estreno': 2018, 'recaudacion':'1.150miles de millones'},
   {'name': 'Linterna Verde', 'valoracion del publico': 4, 'anio de estreno': 2011, 'recaudacion':'219millones'},
]


for pelicula in peliculas:
    lista_peliculas.insertar(Pelicula(pelicula['name'],
                                           pelicula['valoracion del publico'],
                                           pelicula['anio de estreno'],
                                           pelicula['recaudacion']), 'nombre')        

lista_peliculas.barrido() 
print()     

#!a
anio_aux = input('ingrese un año para realizar el filtro')

if (pelicula['anio de estreno'] == anio_aux):
    print('las peliculas que se estrenaron ese anio son:', pelicula['name'])  
else:
    print('no se estrenaron peliculas ese año')

#!b
lista_peliculas.barrido_mayor_recaudado()

#!c
lista_peliculas.barrido_mayor_valoracion()

#!d
lista_peliculas_aux= Lista()
for pelicula in peliculas:
    lista_peliculas_aux.insertar(Pelicula(pelicula['name'],
                                           pelicula['valoracion del publico'],
                                           pelicula['anio de estreno'],
                                           pelicula['recaudacion']), 'nombre') 

lista_peliculas_aux.barrido_lista()
print()