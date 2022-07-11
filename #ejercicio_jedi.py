#ejercicio_jedi.py
from listas import Lista

class Jedi:
    
    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"


lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('jedis.txt')
lineas = file.readlines()

lista = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    datos.pop(-1)
    # print(datos[4].split('/'))
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')
    lista.append(Jedi(datos[0],
                      datos[2],
                      datos[3].split('/'),
                      datos[4].split('/')))
# !
lista_jedi.barrido()
print()
# lista_jedi2.barrido()

dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')

print()
lista_jedi.barrido_jedi_master()

print()
lista_jedi.barrido_comienza_con(['a'])
# for jedi in lista:
#     print(jedi)

#!f
lista_jedi.barrido_sable_luz_color()
print()
lista_jedi2.barrido_sable_luz_color()
print()

#!g

if(dato.sable_luz == 'amarillo' or 'violeta'):
    print({dato.info})

#!h

if(dato.maestro == 'Qui-Gon Jin' and 'Mace Windu'):
    print('los nombres de los padawan son:',dato.nombre )