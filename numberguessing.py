import random

trys = 3
mytry = 1

while mytry <= trys:

    #create random number between 1 and 10
    rndnum = random.randint(1, 10)

    #the user number
    guessnum = int(input(">>>"))

    if guessnum == rndnum:
        print(f"You win!\nThe number is {rndnum}")
        break
    else:
        if mytry != 3:
            print("False, try again")
            mytry += 1

        else:  #capture the last try
            print(f"False!\nThe number was {rndnum}")
            break