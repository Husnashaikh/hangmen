import random
def hangman():
    list_of_words=["navgurkul","kindness","india","hangman"]
    word=random.choice(list_of_words)
    turns=10
    guessmade=""
    valid_entery=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        mainword=""
        missed=0
        for letter in word:
            if letter in guessmade:
                mainword=mainword+letter
            else:
                mainword=mainword+"_ "
        if mainword==word:
            print(mainword)
            print("YOU WON..!!!!")
            break
        print("guess",mainword)
        guess=input()
        if guess in valid_entery:
            guessmade=guessmade+guess
        else:
            print("enter vaild character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left!!!")
                print("--------------")
            if turns==8:
                print("8 turns left!!!")
                print("---------------")
                print("       O       ") 
            if turns==7:
                print("7 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns==6:
                print("6 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("       /       ")
            if turns==5:
                print("5 turns left!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns==4:
                print("4 turns left!!!")
                print("---------------")
                print("      \O       ")
                print("       |       ")
                print("      / \      ")
            if turns==3:
                print("3 turns left!!!")
                print("---------------")
                print("      \O/      ")
                print("       |       ")
                print("      / \      ")
            if turns==2:
                print("2 turns left!!!")
                print("---------------")
                print("      \O/ |    ")
                print("       |       ")
                print("      / \      ")
            if turns==1:
                print("only 1 turns left!!! man is on his last breath")
                print("---------------")
                print("      \O/_|    ")
                print("       |       ")
                print("      / \      ")
            if turns==0:
                print("you losse")
                print("you let a good man die")
                print("---------------")
                print("       O_|    ")
                print("      /|\     ")
                print("      / \      ")
                print("the man is hanged....!")
                break
name=input("enter the name:-")
print("welcome",name,"!")
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()