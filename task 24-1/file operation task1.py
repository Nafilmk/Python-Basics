#Write a Python program to read and write an entire text file.
with open('task1.txt','w')as f:
    f.write('hello world')
f=open('task1.txt')
print(f.read())
f.close()