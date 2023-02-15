with open('write.txt','w')as f:
    a='hello maitexa'
    f.write(a)
    f=open('write.txt')
print(f.readlines())
    