#!/usr/bin/python3
from binascii import unhexlify

ciphertext = unhexlify("4b4e4f42504c4d445c4f7173637f6161774e79764b7e7f65714662746e7270787f4a477c4f4448464654")
plaintext = ""

for i in range(len(ciphertext)):
    plaintext += chr(i ^ ord(ciphertext[i]))
print("Flag : {0}".format(plaintext.encode()))
