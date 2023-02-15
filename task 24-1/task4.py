#Count number of lines in a text file in Python
f=open('task1.txt')
lines=len(f.readlines())
print('total number of line :',lines)