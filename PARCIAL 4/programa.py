"""
Una compañía que vende productos alimenticios desea un programa en Python que permita cargar y administrar los datos de
las operaciones realizadas. Por cada producto vendido se conoce: su código identificatorio (un entero), su peso (un número float),
el tipo de alimento (un número entero que puede tomar valores del 0 al 19 ambos incluidos, por ejemplo: 0: lácteo,
1: derivado de la carne, etc.), el lugar de procedencia (un número entero entre 1 y 20, por ejemplo: 0: Sur de Córdoba,
1: Norte de Buenos Aires, etc.) y su precio de venta (un float). Se pide definir el tipo Producto con los campos pedidos,
y desarrollar un programa en Python controlado por un menú de opciones que permita gestionar las siguientes tareas:

1- Cargar un arreglo de registros con los datos de n productos vendidos. Valide los campos que sea necesario.
Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual,
y si la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre quede ordenado de
menor a mayor por código de identificación. Para esto debe utilizar el algoritmo  inserción ordenada con búsqueda binaria.
Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el
algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el contenido completo del vector a razón de un registro por línea, pero muestre solo los registros cuyo precio de
venta esté incluido entre los valores p1 y p2 que se cargan por teclado.

3- A partir del vector de registros, genere una matriz para acumular las cantidades disponibles de stock por cada combinación
entre tipo de producto y por lugar de origen (o sea, 20 * 20 acumuladores en una matriz de acumulación). Muestre solo los
acumuladores cuyo valor final sea menor a un valor t que se carga por teclado.

4- A partir del vector de registros, genere un archivo binario que contenga los datos de los registros cuyo lugar de origen
no sea 8, y cuyo peso sea menor a un valor p que se carga por teclado.

5- Muestre el contenido del archivo, a razón de un registro por línea. Al final del listado muestre una línea adicional
con el peso promedio de todos los productos mostrados.


"""
from registros import Producto
import registros
import random
import os.path
import pickle



def add_in_order(reg, vec):
    n = len(vec)
    pos = n
    izq, der = 0, n-1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == reg.codigo:
            pos = c
            break
        if reg.codigo < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [reg]


def mostrar_menu(opc):
    for i in opc:
        print(i)
    return

def opcion2(x, y, vec):
    for i in range(len(vec)):
        if x < vec[i].importe < y:
            print(' - Codigo: ',vec[i].codigo, end =' ')
            print(' - Peso: ', vec[i].peso, end=' ')
            print(' - Tipo: ', vec[i].tipo, end=' ')
            print(' - Lugar: ', vec[i].lugar, end=' ')
            print(' - Importe: ', vec[i].importe)

def opcion4(vec):
    NOMBRE_ARCHIVO = input('Ingrese el nombre del archivo a crear: ')
    arch = open(NOMBRE_ARCHIVO, 'wb')
    p = int(input('Ingrese el peso al que deben ser menores los productos a agregar al archivo: '))

    for i in range(len(vec)):
        if vec[i].lugar != 8 and vec[i].peso < p:
            pickle.dump(vec[i], arch)

    arch.close()
    return NOMBRE_ARCHIVO

'''5- Muestre el contenido del archivo, a razón de un registro por línea. Al final del listado muestre una línea adicional
con el peso promedio de todos los productos mostrados.'''

def opcion5(name):
    weight = 0
    n = 0
    arch = open(name, 'rb')
    tam = os.path.getsize(name)
    while arch.tell() < tam:
        reg = pickle.load(arch)
        print(' - Codigo: ', reg.codigo, end=' ')
        print(' - Peso: ', reg.peso, end=' ')
        print(' - Tipo: ', reg.tipo, end=' ')
        print(' - Lugar: ', reg.lugar, end=' ')
        print(' - Importe: ', reg.importe)
        n += 1
        weight += reg.peso
    print('El peso promedio fue:', round(weight/n, 2))
def principal():

    vec_productos = []

    opciones = (' ',
                '--MENÚ DE OPCIONES--',
                ' ',
                '0 - Salir',
                '1 - Cargar arreglo de productos',
                '2 - Mostrar vector de registros',
                '3 - Filtrar con matriz',
                '4 - Generar archivo Binario',
                '5 - Mostrar archivo',)


    opc = -1
    while opc != 0:
        mostrar_menu(opciones)
        opc = int(input("Elija su opcion: "))

        if opc == 0:
            print("Gracias por usar el pro1grama :)")

        elif opc == 1:
            x = int(input("Cuantos productos quiere generear aleatoriamente? ", ))
            for i in range(x):
                reg = registros.crear_aleatorio()
                add_in_order(reg, vec_productos)

        elif opc == 2:
            print("Ingrese entre que números debe de estar el precio de los productos: ")
            x = int(input('Primer numero: '))
            y = int(input("Segundo numero: "))
            while y < x:
                print('El primer numero debe ser menor al segundo, intente otra vez...')

                x = int(input('Primer numero: '))
                y = int(input("Segundo numero: "))

            opcion2(x, y, vec_productos)

        #elif opc == 3:

        elif opc == 4:
            nombre_arch = opcion4(vec_productos)

        elif opc == 5:
            opcion5(nombre_arch)


if __name__ == '__main__':
    principal()
