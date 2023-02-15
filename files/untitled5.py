with open('write.txt','a')as f:
    f.write("\nhello")
    f.write('\nnafil')
    f.close()
f=open('write.txt')
print(f.read())
    