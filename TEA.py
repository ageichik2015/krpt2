import sys
from ctypes import *

def encrypt(text, key):
    y = c_uint32(text[0])
    z = c_uint32(text[1])
    sum = c_uint32(0)
    delta = 0x9e3779b9
    n = 32
    w = [0,0]

    while(n>0):
        sum.value += delta
        y.value += ( z.value << 4 ) + key[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + key[1]
        z.value += ( y.value << 4 ) + key[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + key[3]
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

def decrypt(text, key):
    y = c_uint32(text[0])
    z = c_uint32(text[1])
    sum = c_uint32(0xc6ef3720)
    delta = 0x9e3779b9
    n = 32
    w = [0,0]

    while(n>0):
        z.value -= ( y.value << 4 ) + key[2] ^ y.value + sum.value ^ ( y.value >> 5 ) + key[3]
        y.value -= ( z.value << 4 ) + key[0] ^ z.value + sum.value ^ ( z.value >> 5 ) + key[1]
        sum.value -= delta
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w

if __name__ == "__main__":
    key = [1,2,3,4]
    print("Ключ -",key)
    text = [0,0]
    text[0]=int(input("v0="))
    text[1]=int(input("v0="))
    enc = encrypt(text,key)
    print("Зашифровано: ",enc)
    print("Расшифровано: ",decrypt(enc,key))
