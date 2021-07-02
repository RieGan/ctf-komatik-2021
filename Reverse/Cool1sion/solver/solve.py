charset = 'qwertyuiopasdfghjklzxcvbnm'

res = {}
res2 = {}
for i in charset:
    for j in charset:
        for k in charset:
            for l in charset:
                tmp = ord(i) ^ ord(j)
                tmp *= ord(k)
                tmp += ord(l)
                tmp ^= (ord(i)**3)
                tmp *= ord(i)
                tmp -= ord(k)
                tmp %= 0xffffff
                res[i,j,k,l] = tmp
                if(tmp in res2.keys()):
                    print('found collision')
                    print([i,j,k,l])
                    print(res2[tmp])
                    exit()
                else:
                    res2[tmp] = [i,j,k,l]

"""
First String: yiwqyiwqyiwqyiwqyiwqyiwq
Second String: tveltveltveltveltveltvel
KOMATIKCTF{simple_hash_collision_is_pretty_cool_right}
"""