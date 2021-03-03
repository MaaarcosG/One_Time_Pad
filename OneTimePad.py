import random
import os
import string
import bitarray
import sys


def string_to_bitarray(data):
    msg_bitarray = bitarray.bitarray()
    msg_bitarray.frombytes(data.encode('utf-8')) 
    return msg_bitarray

def bit_to_string(data):
    return ''.join(chr(int(data[i*8:i*8+8],2)) for i in range(len(data)/8))

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

    #Para binario 1 y 0
    msg_cifrado = xor(msg_array, key_array).to01()
    key_gene = key_array.to01()

    # retorna en bytes el mensaje cifrado y la llave generada
    return msg_cifrado, key_gene
    
def decrypt(cypher, key):
    cypher_array = bitarray.bitarray(cypher)
    key_array = bitarray.bitarray(key)

    msg_descifrado = xor(cypher_array, key_array).tobytes().decode('utf-8')

    return msg_descifrado

def get_encrypt_file(filename):
    data_encrypt = open(filename, 'r').read()
    (plaintext, key) = encrypt(data_encrypt)
    
    with open('cypher.txt', 'w+') as file:
        file.write(plaintext)
        
    with open('key.txt', 'w+') as file:
        file.write(key)

def get_decrypt_file(filename, key_file):
    msg = open(filename, 'r').read()
    key = open(key_file, 'r').read()
        
    msg_descrypt = decrypt(msg, key)
        
    with open('decrypt.txt', 'w') as file:
        file.write(msg_descrypt)


if __name__ == '__main__':
    if(len(sys.argv) == 2):
        get_encrypt_file(sys.argv[1])

    else:
        get_decrypt_file(sys.argv[1], sys.argv[2])
