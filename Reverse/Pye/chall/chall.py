#!/usr/bin/python3
from secret import flag
from binascii import hexlify

ciphertext = ""
plaintext = flag

for i in range(len(plaintext)):
    ciphertext += chr(i ^ ord(plaintext[i]))
print("Ciphertext : {0}".format(hexlify(ciphertext.encode()).decode()))
