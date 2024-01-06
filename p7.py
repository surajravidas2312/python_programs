import os
os.chdir("/home/mca/Desktop/SURAJ-MCA/PYTHON/C05")
try:
    f=open("file1.txt","r")
    s=f.read()
    print(s)
    print("try part")
finally:
    print("final Part")

