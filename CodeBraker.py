import random
import numpy as np


def RandomFourDigits():
    #code generates 4 random digits 
    FourNumGen=[str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))]
    FourNum="".join(FourNumGen)
    print(f"Generated code :{FourNum}(*imagine you havent seen it, it just to make your life easier)")
    return FourNum

ComputerFourNumbers=RandomFourDigits()
userChoice=""


def UserFourNumb():
    #User picks 4 digits
    print("Jot down 4 numbers:")
    print("*******************")
    userChoice=input()
    correctInput=True
    while correctInput:
        if userChoice.isdigit():
            if len(userChoice)==4:
                print("*******************")
                correctInput=False
            else:
                print("Only 4 digits!")
                userChoice=input()
        else:
            print("Only digits!")
            userChoice=input()
    return userChoice




def EqualNumbers():
    # True and False value arrey in case of similar numbers
    global ComputerFourNumbers
    global UserFourNumbers

    ComputerNumbArray=[*ComputerFourNumbers]
    UserNumbArray=[*UserFourNumbers]

    TFmassive = np.in1d(ComputerNumbArray,UserNumbArray)
    SameNumb=0
    i=0
    #return amount of equal numbers
    while i<len(TFmassive):
        if TFmassive[i]:
            SameNumb+=1
            i+=1
        else:
            i+=1
    print(f"{SameNumb} of your numbers are presented in genereted code")
    return SameNumb




def EqualPositions():
    #returns amount of digits which are placed in correct positions 
    global ComputerFourNumbers
    global UserFourNumbers
    ComputerFourNumbersArray=[*ComputerFourNumbers]
    UserFourNumbersArray=[*UserFourNumbers]
    SamePosition=0
    i=0
    while i<4:
        if ComputerFourNumbersArray[i]==UserFourNumbersArray[i]:
            SamePosition+=1
            i+=1
        else:
            i+=1
    print(f"{SamePosition} numbers are placed in correct order")
    return SamePosition

def GameStarts(SameNumb, SamePosition, UserFourNumbers):
    Finish=True
    tries=12
    while Finish:
        if tries>1:
            if SameNumb==4 and SamePosition==4:
                print("You broke the code!")
                Finish=False
            else:
                tries-=1
                print(f"***********************")
                print(f"You have left {tries} tries")
                print(f"***********************")
                UserFourNumbers=UserFourNumb()
                SameNumb=EqualNumbers()
                SamePosition=EqualPositions()
                Finish=True
        else:
            print("Code has not been borken")
            Finish=False
            

UserFourNumbers=UserFourNumb()
SameNumb=EqualNumbers()
SamePosition=EqualPositions()
GameStarts(SameNumb, SamePosition, UserFourNumbers)

