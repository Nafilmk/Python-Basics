with open("data.txt",'w')as f:
    a=["Apple","Banana","Apricot","Jackfruit","Jujube","Honeydew","melon","Kiwi","Kabosu","Lime","Lychee","Mango","Mulberry"]
    for i in range(0,10):
        for i in a:
            f.write(i+"\n")