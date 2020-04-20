from time import sleep
import sys

lines  = ["Welcome to Quiz game BETA version!\nin this version i will give only 3 question"]
for line in lines:
    for c in line:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.1)
    print('')
sleep(1)

for attempt in range(0,99):
    quiz1 = ["1.Who make this program??"]
    for line in quiz1:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')
    answer = input("Your answer is :")

    quiz2 = ["2.Who is my best friend??"]
    for line in quiz2:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')
    answer2 = input("Your answer is :")

    quiz3 = ["3.What language that i use to make this program??"]
    for line in quiz3:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')
    answer3 = input("Your answer is :")

    if answer in "Linkachus17" and answer2 in "Ramzi" and answer3 in "Python":
        print("Great job!")
        sleep(1)
    else:
        print("Your answer is incorrect!")
        print("Which one? i don't know man!")
        sleep(2)