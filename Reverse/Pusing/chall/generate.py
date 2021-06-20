import os
from secret import flag
for i in range(50):
    key = os.urandom(len(flag))
    f = open('./key/key{0}'.format(i),'w')
    f.write(key)
    f.close()