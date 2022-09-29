
import random

rps = ["Rock", "Paper", "Scissors"]
num_tries = 0 #number of tries counter
pcwins = 0 #number of pc wins counter
playerswins = 0 #number of player wins counter
tie = 0  #number of ties counter

try_again = "y" #try again variable

while try_again == "y":
    num_tries = num_tries + 1          
    comp = (random.choice(rps))
    user_rps = input("Enter Rock, Paper or Scissors: ")
    #Captialing of the first letter rock, paper & scissors
    user_rps = (user_rps.capitalize())
    print (f"You selected: {user_rps}")
    print (f"Computer selected: {comp}")

    print()

    if (comp) == 'Rock' and (user_rps) == 'Paper':
        print (f"{user_rps} --> You win")
        playerswins = playerswins+1
    elif (comp) == 'Paper' and (user_rps) == 'Rock':
        print (f"{comp} --> PC wins")
        pcwins = pcwins+1

    #Rock-Scissors sections
    if (comp) == 'Rock' and (user_rps) == 'Scissors':
        print (f"{user_rps} --> You win")
        playerswins = playerswins + 1
    elif (comp) == 'Scissors' and (user_rps) == 'Rock':
        print (f"{comp} --> PC wins")
        pcwins = pcwins + 1

    #Scissors-Paper sections
    if (comp) == 'Paper' and (user_rps) == 'Scissors':
        print (f"{user_rps} --> You win")
        playerswins = playerswins + 1
    elif (comp) == 'Scissors' and (user_rps) == 'Paper':
        print (f"{comp} --> PC wins")
        pcwins = pcwins + 1

    #It's a tie sections
    if (comp) == 'Rock' and (user_rps) == 'Rock':
        print ("It's a tie")
        tie = tie + 1
    elif (comp) == 'Scissors' and (user_rps) == 'Scissors':
        print ("It's a tie")
        tie = tie + 1
    elif (comp) == 'Paper' and (user_rps) == 'Paper':    
        print ("It's a tie")
        tie = tie + 1

    try_again = input("Would like to play again y or n: ") #A user trying again

    if try_again == ("y"):
        continue

#Total sums of everything   

print()
print (f"Number of attempts: {num_tries}")
print (f"Number of PC Wins: {pcwins}")
print (f"Number of Your Wins: {playerswins}")
print (f"Number of Ties: {tie}")

