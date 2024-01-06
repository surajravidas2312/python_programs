import os
os.chdir("/home/mca/Desktop/SURAJ-MCA/PYTHON/C05")
f=open("file1.txt","w")
print(f.name,"created")
f.write("Hello World !")
f.close()
print("txt added")
