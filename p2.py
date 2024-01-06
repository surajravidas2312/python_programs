import os
os.chdir("/home/mca/Desktop/SURAJ-MCA/PYTHON/C05")
f=open("abc.txt","w")
f.write("My First Text.\nThis is my python program.")
f.close()

print("File opened and value in file printed")
f=open("abc.txt","r")
str=f.read()
print(str)
f.close()
print("f closed")


