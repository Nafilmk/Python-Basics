#Write a Python program to append text to a file and display the text.
with open('task1.txt','a+')as f:
    f.write('\nhi nafil')
with open('task1.txt')as f:
    print(f.read())
    f.close()