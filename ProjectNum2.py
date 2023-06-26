import random
import time
import string

alphabet = string.ascii_lowercase
alpha_list = list(alphabet)
print("Welcome to 'Writing Speed' test ")
print("Please enter 5 words ")
for trial in range(5):
    input("Enter a word : ")
while True:
    file = open("writing.txt", "a")
    x = input("Please Select 1 or 2 \n 1- Write a word \n 2- Test your Writing Speed ")
    if x == "1":
        for word in range(5):
            input("Please enter a word : ")
    elif x == "2":
        input("Press Enter When You're Ready")
        a = random.choice(alpha_list)
        b = random.choice(alpha_list)
        c = random.choice(alpha_list)
        d = random.choice(alpha_list)
        e = random.choice(alpha_list)
        print(a, b, c, d, e)
        start = time.time()
        l = list(input())
        end = time.time()
        t = str(end - start)
        if l == [a, " ", b, " ", c, " ", d, " ", e]:
            file.write(a + " ," + b + " ," + c + " ," + d + " ," + e + " ," "True " + t + "\n")
            print("True", t)
        else:
            file.write(a + " ," + b + " ," + c + " ," + d + " ," + e + " ," + "False " + t + "\n")
            print("NO", t)
    else:
        print("Wrong Entry")
    file.close()










