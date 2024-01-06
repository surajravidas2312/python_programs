import os
os.chdir("/home/mca/Desktop/SURAJ-MCA/PYTHON/C05")
f=open("abc.txt","w")
f.write("My First Text.")
f.close()
print("file",f.name,"closed")
