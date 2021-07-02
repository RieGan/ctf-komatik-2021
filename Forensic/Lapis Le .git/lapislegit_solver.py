import os
import time

flag = ""
for i in range(0,30):
    os.system("git reset --hard HEAD~1")
    time.sleep(0.3)
    f = open("./flag.txt")
    time.sleep(0.3)
    flag = f.read().strip() + flag
    time.sleep(0.3)
    print(flag)
