import time
with open("data.txt")as f:
    for i in f:
        if (i=='melon\n'):
            continue
        print(i)
        time.sleep(1)