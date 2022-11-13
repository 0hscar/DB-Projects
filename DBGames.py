
from re import I
import random
from threading import Timer
from unittest import expectedFailure
import os


'''RPS Variables'''
rpsChoices = [1,2,3]
rpsChoicesNames = ["Rock", "Scissors", "Paper"]
playerScore = int(0)
computerScore = int(0)

'''Mind Reader Variables'''

'''Optimus Prime Variables'''

'''Game Functions'''
def cls():
    os.system("cls" if os.name =="nt" else 'clear')


    

dcls = Timer(3, cls)

'''RSP Functions'''
def rspCheckResult(player1, player2, player, computer):
    roundWinner = 0
    if player in (rpsChoices):
        if player == computer:
            print("\nDraw!")
        elif player == 1 and computer == 2:
            # print("\n", player1,"chose rock,", player2,"chose scissors,", player1,"won!")
            roundWinner = 1
        elif player == 1 and computer == 3:
            # print("\n", player1,"chose rock,", player2,"chose paper,", player2,"won!")
            roundWinner = 2
        elif player == 2 and computer == 1: 
            # print("\n", player1,"chose scissors,", player2,"chose rock,", player2,"won!")
            roundWinner = 2
        elif player == 2 and computer == 3:
            # print("\n", player1,"chose scissors,", player2,"chose paper,", player1,"won!")
            roundWinner = 1
        elif player == 3 and computer == 1:
            # print("\n", player1,"chose paper,", player2,"chose rock,", player1,"won!")
            roundWinner = 1
        elif player == 3 and computer == 2:
            # print("\n", player1,"chose paper,", player2,"chose scissors,", player2,"won!")
            roundWinner = 2
    else:
        print("\nPlease choose between (1:Rock) (2:Scissors) (3:Paper)\n")
    return roundWinner
        
'''Mind Reader Functions'''

'''Optimus Prime Functions'''

'''Main Code'''
while True:
    cls()
    print("\n**********\nMain Menu\n**********")
    MenuChoice = input("What do you want to play? :\nRPS, Mind Reader or Optimus Prime (no caps)\n")
    
    if MenuChoice == "exit":
        print("Leaving...")
        break
    
    elif MenuChoice == "rps":
        '''RPS Game Code'''
        cls()
        while True:
            print("\n***************\nWelcome to RPS!\n***************")
            player1 = input("Player 1 name: ")
            player2 = input("Player 2 name: (enter a zero if you want to play against computer) ")
            if player2 == "0":
                player2 = "Computer"
            while True:
                try:
                    rounds = int(input("To how many points do you want to play?: "))
                    break
                except:
                    print("Not a number")
            cls()
            while playerScore<rounds and computerScore<rounds:
              
                
                print("\n",player1, ":", playerScore, "\n",player2,":",computerScore,"\n")
                        
                playerChoice = input(F"{player1} choose: \n1:Rock\n2:Scissors\n3:Paper\n")
                computerChoice = input(F"{player2} choose: \n1:Rock\n2:Scissors\n3:Paper\n") if player2 != "Computer" else str(random.randint(1,3)) 
                #Changes the random to string so I can check them both in the if statement, otherwise I would have seperate checks for them
                cls()
                if playerChoice == "exit" or computerChoice == "exit":
                    print("Leaving...")
                    break
                elif playerChoice.isdigit() and computerChoice.isdigit():
                    roundWinner = rspCheckResult(player1, player2, int(playerChoice), int(computerChoice))
                    
                    if roundWinner == 1:
                        print(player1, "chose", rpsChoicesNames[int(playerChoice)-1], ",", player2, "chose", rpsChoicesNames[int(computerChoice)-1], ":", player1, "won the round!")
                        playerScore += 1
                    elif roundWinner == 2:
                        print(player1, "chose", rpsChoicesNames[int(playerChoice)-1], ",", player2, "chose", rpsChoicesNames[int(computerChoice)-1], ":", player2, "won the round!")                      
                        computerScore += 1
                    
                else:
                    print("Invalid input")
                
                
            print("\nWinner: ", player1 if playerScore > computerScore else player2)
            if input("\nDo you want to play again? (1: Yes, Anything else: No): ") == "1":
                computerScore = 0
                playerScore = 0
                continue
            else: break
        
    elif MenuChoice == "mind reader":
        '''Mind Reader Code'''
        cls()
        while True:
            print("\nWelcome to Mind Reader!\n")
            while True:
                try:
                    diff = int(input("Difficulty 1: 1-10\nDifficulty 2: 1-20\nDifficulty 3: 1-30\nPlease select a difficulty (1-3): "))
                    break
                except:
                    print("Input not a number")
            print("\nGo ahead, try to guess the number I am thinking about")
            randNumber = random.randint(1,diff*10)
            guesses = 0
            cls()   
            while True:
                             
                userGuess = input("Guess: ")
                if userGuess == "exit":
                    print("Leaving...")
                    break
                elif userGuess.isdigit():
                    if int(userGuess) == randNumber:
                        print("\nYou chose wisely, well done!\nIt took you", guesses+1,"guess(es) to get it right.")
                        break
                    print("You need to go", 'higher' if int(userGuess) < randNumber else 'lower')
                    guesses += 1
                    print("Guesses:", guesses, "\n")
                    
                else:
                    print("Incorrect input")
                
            if input("\nDo you want to play again (1: Yes, Anything else: No): ") == "1":
                continue
            else: break 
        

    elif MenuChoice == "optimus prime":
        '''Optimus Prime Code'''        
        
    else:
        print("Please type one of the above!")