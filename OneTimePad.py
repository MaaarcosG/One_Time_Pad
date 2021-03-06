import random
import os
import string
import bitarray
import sys


def string_to_bitarray(data):
    msg_bitarray = bitarray.bitarray()
    msg_bitarray.frombytes(data.encode('utf-8')) 
    return msg_bitarray

def xor(msg_array, key_array):
    data_array = []
    for x in range(len(msg_array)):
        valor = msg_array[x] ^ key_array[x] 
        data_array.append(valor)
    return bitarray.bitarray(data_array)

def generate_key(data):
    key = []
    for _ in range(data):
        key.append(random.choice(['0', '1']))

    return ''.join(key)

def encrypt(msg):
    msg_array = string_to_bitarray(msg)
    key_array = string_to_bitarray(generate_key(len(msg)))

    #Para binario 1 y 0
    msg_cifrado = xor(msg_array, key_array).to01()
    key_gene = key_array.to01()

    return msg_cifrado, key_gene
    
def decrypt(cypher, key):
    cypher_array = bitarray.bitarray(cypher)
    key_array = bitarray.bitarray(key)

    msg_descifrado = xor(cypher_array, key_array).tobytes().decode('utf-8')

    return msg_descifrado

def get_encrypt_file(filename):
    # abrimos el archivo
    data_encrypt = open(filename, 'r').read()
    (plaintext, key) = encrypt(data_encrypt)
    
    with open('cypher.txt', 'w') as file:
        file.write(plaintext)
        
    with open('key.txt', 'w') as file:
        file.write(key)

def get_decrypt_file(filename, key_file):
    msg = open(filename, 'r').read()
    key = open(key_file, 'r').read()
        
    msg_descrypt = decrypt(msg, key)
        
    with open('decrypt.txt', 'w') as file:
        file.write(msg_descrypt)

def create_txt(msg: str):
    with open('text.txt', 'w+') as file:
        file.write(msg)

if __name__ == '__main__':
    while True:
        opcion = input('Bienvenidos!\n 1. Encriptar\n 2. Desencriptar\n 3. Salir\nEscoga lo que quiere hacer: ')
        
        if opcion == '1':
            print('*'*40)
            msg = input('Escriba el mensaje que desea mandar: ')
            with open('text.txt', 'w') as file:
                file.write(msg)
            
            print(' ARCHIVO text.txt CREADO CORRECTAMENTE\n MENSAJE ENCRIPTADO')
            get_encrypt_file('text.txt')
            break

        elif opcion == '2':
            print('*'*40)
            filename = input('Ingrese el nombre del archivo encriptado: ')
            key_file = input('Ingrese el nombre con la llave: ')
            get_decrypt_file(filename, key_file)
            break
        
        else:
            break
    
    '''
    PARA RECIBIR DE CONSOLA
    if(len(sys.argv) == 2):
        get_encrypt_file(sys.argv[1])

    else:
        get_decrypt_file(sys.argv[1], sys.argv[2])
    '''


