with open("data2.txt")as f:
    for i in f:
        if (i=='Banana\n'):
            break
        print(i)