import random
import os
import string
import bitarray
import sys


def string_to_bitarray(data: str):
    array = bitarray.bitarray()
    array.frombytes(data.encode('utf-8'))
    return array
    
def xor(msg_array, key_array):
    data_array = []
    for x in range(len(msg_array)):
        valor = msg_array[x] ^ key_array[x] 
        data_array.append(valor)
    return bitarray.bitarray(data_array)

def generate_key(data):
    key = []
    for _ in range(data):
        key.append(random.choice(string.printable))
    
    key = ''.join(key)
    #print(key)
    return key

def encrypt(msg):
    msg_array = string_to_bitarray(msg)
    key_array = string_to_bitarray(generate_key(len(msg)))

    msg_cifrado = xor(msg_array, key_array).tobytes().decode('utf-8')
    key_gene = key_array.tobytes().decode('utf-8')

    # retorna en bytes el mensaje cifrado y la llave generada
    return msg_cifrado, key_gene
    
def decrypt(cypher, key):
    cypher_array = bitarray.bitarray()
    cypher_array.frombytes(cypher.encode('utf-8'))
    key_array = bitarray.bitarray()
    key_array.frombytes(key.encode('utf-8'))

    # retornamos el mensaje descifrado
    msg_descifrado = xor(cypher_array, key_array).tobytes().decode('utf-8')

    return msg_descifrado

def get_encrypt_file(filename):
    try:
        data_encrypt = open(filename, 'r').read()
        
        (plaintext, key) = encrypt(data_encrypt)
        
        with open('cypher.txt', 'w') as file:
            file.write(plaintext)
            
        with open('key.txt', 'w') as file:
            file.write(key)
    except:
        print('Error: %s' % sys.exc_info()[0])

    
def get_decrypt_file(filename, key_file):
    try:
        msg = open(filename, 'r').read()
        key = open(key_file, 'r').read()
        
        msg_descrypt = decrypt(msg, key)
        
        with open('decrypt.txt', 'w') as file:
            file.write(msg_descrypt)
    except:
        print('Error: %s' % sys.exc_info()[0])

if __name__ == '__main__':
    if(len(sys.argv) == 2):
        get_encrypt_file(sys.argv[1])

    else:
        get_decrypt_file(sys.argv[1], sys.argv[2])
