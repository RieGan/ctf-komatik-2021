import os
import time

os.system("git init .")
time.sleep(0.3)

flag = "KOMATIKCTF{G1t_R3s3t_l0op}"
print(os.listdir())
for ch in flag:
    command = "echo " + ch + " > flag.txt"
    # print(command)
    os.system(command)
    time.sleep(0.3)
    os.system("git add flag.txt")
    time.sleep(0.3)
    os.system("git commit -m update")
    time.sleep(0.3)

os.system("rm flag.txt")
time.sleep(0.3)
os.system("git add .")
time.sleep(0.3)
os.system("git commit -m removeflag")
