import os
os.chdir("/home/mca/Desktop/SURAJ-MCA/PYTHON/C05")


print("File opened and value in file printed")
f=open("abc.txt","r")
str=f.read()
print(str)
f.close()
print("f closed")


