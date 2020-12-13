import random

def gameWin(comp, you):
    if comp == 1:
        if you == 3:
            return False

        elif you == 2:
            return True

        elif you == comp:
            return None

        else: 
            return a

    elif comp == 2:
        if you == 1:
            return False

        elif you == 3:
            return True

        elif you == comp:
            return None

        else: 
            return a

    elif  comp == 3:
        if you == 2:
            return False

        elif you == 1:
            return True

        elif you == comp:
            return None

        else: 
            return a

    
randomNumber = random.randint(1,3)

print("Computer's turn: Choose Rock(1) Paper(2) or Scissors(3)\n")
comp = randomNumber
you = int(input("Your turn: Choose Rock(1) Paper(2) or Scissors(3)\n"))

a = f"######### {you} is Wrong Input. Choose 1, 2 or 3! ############# \n"


c = gameWin(comp, you)
print(f"Computer chose {comp} ")

if c == False:
    print("You lose!!")

elif c == True:
    print("************* Hurray! You win ***************")

elif c == None: 
    print("It's a Draw!")

else: 
    print(a)



