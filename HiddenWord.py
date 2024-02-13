print("Welcome to hang man program!")
print("****************************")
print("Player choose the word:")

#this part make sure that written word doesn't contain any digits within it 
word=input()
IsDigit=True
while IsDigit:
    if word.isalpha():
        IsDigit=False
    else:
        print("Only letters!")
        word=input()


#Here we are creating array of "*" to present them to user 
HiddenWord=len(word)*"*"
lives = 5


def WriteALetter(lives):
    #Here user picks a letter to check and program make sure that input is correct
    print(f"lives left:{lives}")
    UserInput = input("Choose letter:\n")
    IsOneLetter = True
    while IsOneLetter:
        if UserInput.isalpha():
            if len(UserInput) == 1:
                IsOneLetter==False
                return UserInput
            else:
                print("Only 1 letter!")
                UserInput = input("Choose letter:\n")
        else:
            print("Only letters!")
            UserInput=input()




UserLetter=WriteALetter(lives)

def CheckALetter(HiddenWord, lives, UserLetter, word):
    #here is a main sytax of our program, loops and repeateable process of checking letter within user letter array(hidden word) 
    finished=True
    Lives=lives
    HiddenWordOneMoreStar=HiddenWord
    while finished:
        if "*" in HiddenWordOneMoreStar:
            if (UserLetter in word) or (UserLetter.upper() in word) or (UserLetter.lower() in word):
                CharNumb=0
                while CharNumb<len(word):
                    for i in range(len(word)):
                        if UserLetter == word[i-1] or UserLetter.upper() == word[i-1] or UserLetter.lower() == word[i-1]:
                            ArrayHiddenWord=[*HiddenWord]
                            ArrayHiddenWord[i-1]=UserLetter
                            HiddenWord=("".join(ArrayHiddenWord))
                            HiddenWordOneMoreStar=HiddenWord.replace("*","",1)
                            CharNumb+=1
                        else:
                            CharNumb+=1
                else: 
                    print(HiddenWord)
                    UserLetter=WriteALetter(Lives)
            else:
                Lives-=1
                if Lives<=0:
                    print("No more lifes!")
                    exit()
                print("This letter is not in hidden word")
                UserLetter=WriteALetter(Lives)
        else:
            finished=False 
            print(f"The word is {word}, well done!")


CheckALetter(HiddenWord, lives, UserLetter, word)


