import random
import os
import string

range_msg = range(0, 100)

def string_to_ascii(data):
    return [ord(x) for x in data]

def ascii_to_string(data):
    return ''.join(chr(x) for x in data)

def encrypt(msg, filename):
    pass

if __name__ == '__main__':
    while True:
        
        opcion = input('Bienvenidos!\n 1. Encriptar\n 2. Desencriptar\n 3. Salir\nEscoga lo que quiere hacer: ')

        if opcion == '1':
            # mandamos los datos para la funcion
            msg = input('Escriba el mensaje que desea mandar: ')
            filename = input('Ingrese el nombre para el guarda en un archivo el Cyphertext: ')

            encrypt(msg, filename)
            break

        elif opcion == '2':
            print('DESENCRIPTAR')
            
        else:
            print('Adiooos!')
            break
