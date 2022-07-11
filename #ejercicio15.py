#ejercicio15.py
#ejercicio_pokemon
from listas import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas

    def __str__(self):
        return self.nombre

contador=0
class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'juan', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'cris', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'dan', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'antonio', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'steve', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'boltron', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'charizard', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'piyoto', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'magicar', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'bolbazor', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'stilicks', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]


for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista() 
print()   


#! punto a cantidad de pok de un entrenador
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
     print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
else:
     print('el entrenador no esta en la lista')
print()

#!b entrenadores con mas de tres torneos
lista_entrenadores.barrido_entrenador_mas_tres()
print()
#! c
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)
print()

#! d
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador tiene {pos.info}")
    print('sus pokemons')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')
print()

#!e
lista_entrenadores.barrido_porcentaje_victorias()


#!f
lista_entrenadores.barrido_elementos_de_pokemon()

#!g
lista_entrenadores.barrido_promedio_de_nivel()

#!h
for i in range(randint(1, 5)):
    if(pokemon['nombre']=='stilicks'):
        contador=contador + 1

print('la cantidad de entrenadores con pokemones repetidos son:', contador)

#!i
if len(pokemon['name']) == len(set(pokemon['name'])):
    print('no hay pokemones repetidos entre los entrenadores')
else:
    print('los entrenadores con pokemones repetidos son:', lista_entrenadores.busqueda(entrenador['name']))

#!j

if (pokemon['name']=='Tyrantrym', 'Terrakion','Wingull'):
    print('los entrenadores que tienen estos pokemon son:', lista_entrenadores.busqueda(entrenador['name']))

#!k

nombre_del_entrenador_aux = input('ingrese el nombre del entrenador que desea buscar')
nombre_del_pokemon_aux = input('ingrese el nombre del pokemon que decea buscar')

if (nombre_del_entrenador_aux==lista_entrenadores.busqueda(entrenador['name'])):
    print('el entrenador ingresado esta en la lista')
    if(nombre_del_pokemon_aux== pokemon['nombre']):
        print('el pokemon es del entrenador buscado y sus datos son:')
        print(entrenador['name'],entrenador['tg'],entrenador['bp'],entrenador['bg'])
        print(pokemon['name'], pokemon['nivel'], pokemon['tipo'], pokemon['subtipo'])
    else:
        print('el pokemon no esta en la lista')    
else:
    print('el entrenador no se encuentra en la lista')    



