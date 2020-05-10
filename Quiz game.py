import os
from time import sleep


################## DEF #################
def clear():
    os.system('cls')


################ INTRO #################
print(
    "Welcome to trivia game!. this game will give you 10 question and each question has different topics\nYou have 3 "
    "chance to get wrong so becarefull when answering\nAnd the game is case sensitive so becarefull too!")
sleep(3)
clear()
############## QUIZ ####################
for attempt in range(0,3):
    answer1 = input("1.Who made this program?\nYour answer is :")
    clear()
    answer2 = input("2.Who is my best friend?\nYour answer is :")
    clear()
    answer3 = input("3.What language i used to make this game??\nYour answer is :")
    clear()
    answer4 = input("4.Which one is faster? Car or Light?\nYour answer is :")
    clear()
    answer5 = input("5.Which one is light? Cotton or Ant?\nYour answer is :")
    clear()
    answer6 = input("6.Which one is big? Giant or Monster?\nYour answer is :")
    clear()
    answer7 = input("7.Is cabbage a food?\nYour answer is :")
    clear()
    answer8 = input("8.Is salt an ingredient?\nYour answer is :")
    clear()
    answer9 = input("9.Is Butter a food?\nYour answer is :")
    clear()
    answer10 = input("10.Do i have Youtube channel?\nYour answer is :")
    clear()

############## VERIFY ####################
    if answer1 in "Linkachus17" and answer2 in "Ramzi" and answer3 in "Python" and answer4 in "Light" and answer5 in "Cotton" and answer6 in "Giant" and answer7 and answer8 in "Yes" and answer9 in "No" and answer10 in "Yes":
        print("Good job! you passed the trivia!")
        sleep(2)
        break
    else :
        print("Some answer is wrong. if still wrong check your letter case!")
        sleep(2)
        clear()