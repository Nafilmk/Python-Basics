 #Python Program to Copy a File
import shutil
shutil.copyfile('task1.txt','copytask.txt')
f=open('copytask.txt')
print(f.readlines())
f.close()