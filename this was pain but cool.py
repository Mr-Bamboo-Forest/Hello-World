import string
from time import sleep
type = input("Do you want cool or cooler answer 1 for cool and 2 for cooler?: ")

def pain():
    print("Hello World but pain: ")
    for letter in string.ascii_uppercase:
        print(letter, end ="\n")
        sleep(0.015)
        if letter == "H":
            for letter2 in string.ascii_lowercase:
                print("H",letter2, end ="\n")
                sleep(0.015)
                if letter2 == "e":
                    for letter3 in string.ascii_lowercase:
                        print("He",letter3, end ="\n")
                        sleep(0.015)
                        if letter3 == "l":
                            for letter4 in string.ascii_lowercase:
                                print("Hel",letter4, end ="\n")
                                sleep(0.015)
                                if letter4 == "l":
                                    for letter5 in string.ascii_lowercase:
                                        print("Hell",letter5, end ="\n")
                                        sleep(0.015)
                                        if letter5 == "o":
                                            for letter6 in string.ascii_uppercase:
                                                print("Hello ",letter6, end ="\n")
                                                sleep(0.015)
                                                if letter6 == "W":
                                                    for letter7 in string.ascii_lowercase:
                                                        print("Hello W",letter7, end ="\n")
                                                        sleep(0.015)
                                                        if letter7 == "o":
                                                            for letter8 in string.ascii_lowercase:
                                                                print("Hello Wo",letter8, end ="\n")
                                                                sleep(0.015)
                                                                if letter8 == "r":
                                                                    for letter9 in string.ascii_lowercase:
                                                                        print("Hello Wor",letter9, end ="\n")
                                                                        sleep(0.015)
                                                                        if letter9 == "l":
                                                                            for letter10 in string.ascii_lowercase:
                                                                                print("Hello Worl",letter10, end ="\n")
                                                                                sleep(0.015)
                                                                                if letter10 == "d":
                                                                                    print("Hello World!")
                                                                                    print("Hello World!")
                                                                                    return  # Exit the function
                                                                                                                                                                            
def cooler():                                                                                                                                     
    e = 1
    while True:
        e += 1
        pain()
        if e > 2:
            break

def cool():
    a = "hello world"
    b = "abcdefghijklmnopqrstuvwxyz "
    v = ""

    for i in a:
        for j in b:
            if i == j:
                v += j
                print(v)
                break
        sleep(0.2)

if type == "1":
    cool()
elif type == "2":
    cooler()
