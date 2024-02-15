import random 
NumList=[]
i=0

while i<100: 
    NumList.append(random.randint(0,1000))
    i+=1

def OddNumb():
    OddNumb=0
    i=0
    while i<len(NumList):
        if NumList[i]%2==0:
            OddNumb+=1
            i+=1
        else:
            i+=1
    print(f"Odd numbers:{OddNumb}")


def SingleDigit():
    SingleDigits=0
    i=0
    while i<len(NumList):
        if NumList[i]<10:
            SingleDigits+=1
            i+=1
        else:
            i+=1
    print(f"Single digit numbers:{SingleDigits}")

def BiggestNum():
    BiggestNumb=0
    i=0
    while i<len(NumList):
        if NumList[i]>BiggestNumb:
            BiggestNumb=NumList[i]
            i+=1
        else:
            i+=1
    print(f"Biggest number in the list is:{BiggestNumb}")


def SmallestNum():
    SmallestNum=1000000
    i=0
    while i<len(NumList):
        if NumList[i]<SmallestNum:
            SmallestNum=NumList[i]
            i+=1
        else:
            i+=1
    print(f"Smallest number in the list is:{SmallestNum}")

OddNumb()
SingleDigit()
BiggestNum()
SmallestNum()


NumberToFind=input("Jot down number which you want to find!(0-1000):")
InCorrectInput=True
while InCorrectInput:
    if NumberToFind.isdigit():
        if int(NumberToFind)>=0 and int(NumberToFind)<=1000:
            InCorrectInput=False
        else:
            print("Jot down number in range from 0 to 1000!")
            NumberToFind=input()
            InCorrectInput=True
    else:
        print("Only digits!")
        NumberToFind=input()
        InCorrectInput=True

i=0
NumberFound=False
while i<len(NumList):
    if NumList[i]==int(NumberToFind):
        print(f"Position of your number is:{i}")
        NumberFound=True
        i+=1
    elif i<len(NumList)-1:
        i+=1
    else:
        if NumberFound==False:
            print("Number hasn't been found!")
            i+=1
