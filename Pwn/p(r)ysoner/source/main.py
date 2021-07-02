#!/usr/bin/python3 -u
import sys


flag = open('/app/flag.txt', 'r').read()

def split_inp(inp):
    return inp.split(' ')

def validate_input(inp):
    inp = split_inp(inp)
    if(len(inp) != 3):
        return False

    BLACKLIST = [
        'import',
        'ast',
        'eval',
        '=',
        'pickle',
        'os',
        'subprocess',
        'input',
        'sys',
        'print',
        'execfile',
        'builtins',
        'open',
        '_',
        'dict',
        '[',
        '>',
        '<',
        ':',
        ';',
        ']',
        'exec',
        'for',
        'dir',
        'file', 
    ]

    if inp[1] not in ['-', '/', '%']:
        return False

    for i in inp:
        if i in BLACKLIST:
            return False

    return True



print('Calculator that can only substract, divides, and modulo stuff (coz I\'m a programmer)')
sys.stdout.flush()
while True:
    inp  = input('>>> ')
    sys.stdout.flush()
    if(not validate_input(inp)):
        print('what the hell are you trying to do')
        continue
    sys.stdout.flush()
    
    print(eval(inp))