from pwn import *
CHAR = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890}{\'\": ,._'


def printBlock(cipher, length=16):
    for i in range(0, len(cipher), length):
        print(cipher[i:i+length])


if __name__ == '__main__':
    # r = process('../chall/chall.py')
    r = remote('35.187.248.149', 4456)
    awal = 'aaaaa'
    dummy = 'a'*16*5
    target = 'a'*16*5
    payload = awal + dummy + target
    r.sendlineafter('Your name: ', payload)
    r.recvuntil('Token : ')
    cipher = r.recvline()

    text = ''
    while '}' not in text:
        block1 = ''
        block2 = ''
        dummy = dummy[1:80]
        target = target[:-1]
        for char in CHAR:
            padding = dummy + char
            payload = awal + padding + target
            r.sendlineafter('>> ', '2')
            r.sendlineafter('Your name: ', payload)
            r.recvuntil('Token : ')
            cipher = r.recvline()

            if(cipher[32:192] == cipher[192:352]):
                dummy = dummy + char
                text += char
                print(text)
                break
    fullString = 'X'*11 + payload + text