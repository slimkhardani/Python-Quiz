import os
import pickle
import random

def menu():
    while True:
        print("[1] Add new Quiz")
        print("[2] Start Game")
        print("[3] Exit")
        s = int(input(">>> "))
        if 4>s>0:
            break
    if s==1:
        os.system('cls')
        add_quiz()
    elif s==2:
        os.system('cls')
        game()
    else:
        return

def add_quiz():
    if os.path.getsize("db.dat")==0:
        c=[]
    else:
        f=open("db.dat","rb")
        c=pickle.load(f)
        f.close()
    while True:
        question = input("Enter the question : ")
        answers = []
        print("You must enter 4 answer and 1 of them is correct !")
        for i in range(4):
            answer = input("Answer "+str(i+1)+" : ")
            answers.append(answer)
        while True:
            correct_answer = int(input("Which one is correct ? : "))
            if 5>correct_answer>0:
                break
        value=float(input("Value : "))
        q={"q":question,"an":answers,"can":correct_answer,"val":value}
        c.append(q)
        print("Question Added successfully !")
        while True:
            cont = input("There is other question to add ? (o/n) : ")
            if cont=="o" or cont=="n":
                os.system('cls')
                break
        if cont=="n":
            break
    f=open("db.dat","wb")
    pickle.dump(c,f)
    f.close()
    menu()

def game():
    f=open("db.dat","rb")
    c=pickle.load(f)
    f.close()
    lost=False
    left=False
    somme=0
    j=1
    while ((lost==False)and(left==False) and j<=len(c)):
        i=c[j-1]
        print("Question "+str(j)+" : ")
        print(i["q"])
        print("Choose a number between 1 and 4")
        for y in range (4):
            print(str(y+1)+"-"+i["an"][y])
        print("5-I'm Out")
        while True:
            choice=int(input("Your Answer : "))
            if 1<=choice<=5:
                break
        if choice==5:
            left=True
        elif choice!=i["can"]:
            lost=True
        else:
            somme=somme+i["val"]
        j+=1
        if(j>=2) and (j<=10):
            print("Good Job ! Next Round ! \n")
    if (lost==True):
        print("Game Over ! Try Again")
        menu()
    elif (left==True):
        print("You Choose To Leave the Game with "+str(somme)+"TND ! Congrats")
    else:
        print("You're The King Of This Game ")
        print("You Won "+str(somme)+" TND ! ")

menu()