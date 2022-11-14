
import getpass
import math
import os
import random
from re import I
from threading import Timer
from unittest import expectedFailure

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
    

'''RSP Functions'''
def rspCheckResult(player1, player2, player, computer):
    roundWinner = 0
    if player in (rpsChoices):
        if player == computer:
            print("\nDraw!")
        elif player == 1 and computer == 2:
            roundWinner = 1
        elif player == 1 and computer == 3:
            roundWinner = 2
        elif player == 2 and computer == 1: 
            roundWinner = 2
        elif player == 2 and computer == 3:
            roundWinner = 1
        elif player == 3 and computer == 1:
            roundWinner = 1
        elif player == 3 and computer == 2:
            roundWinner = 2
    else:
        print("\nPlease choose between (1:Rock) (2:Scissors) (3:Paper)\n")
    return roundWinner

def choicesGet(input):
    return rpsChoicesNames[int(input)-1]        


'''Mind Reader Functions'''

'''Optimus Prime Functions'''
def checkPrime(userInput):
    for x in range(2, math.floor(math.sqrt(userInput)+1)): #Decreases the range of numbers to check
        if(userInput % x) == 0:
            print("\n",userInput, "is not a prime number")
            break
    else: # Accidental else in for loop, wrong indentation that worked anyway =)
        print("\n",userInput, "is a prime number")
            

'''Main Code'''
while True:
    cls()
    print("\n**********\nMain Menu\n**********")
    MenuChoice = input("What do you want to play? :\n1: RPS, 2: Mind Reader, 3: Optimus Prime or 4: tutorial for info(no caps)\n")
    
    if MenuChoice == "exit":
        print("Leaving...")
        break
    
    elif MenuChoice == "rps" or MenuChoice == "1":
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
                    if rounds < 1:
                        print("No no, none of that here")
                        continue
                    break
                except:
                    print("Not a number")
            cls()
            while playerScore<rounds and computerScore<rounds:
                print("\n",player1, ":", playerScore, "\n",player2,":",computerScore,"\n")
                print("Hidden inputs, don't be afraid when they dont show")
                        
                playerChoice = getpass.getpass(F"{player1} choose: \n1:Rock\n2:Scissors\n3:Paper\n")
                computerChoice = getpass.getpass(F"{player2} choose: \n1:Rock\n2:Scissors\n3:Paper\n") if player2 != "Computer" else str(random.randint(1,3)) 
                #Changes the random to string so I can check them both in the if statement, otherwise I would have seperate checks for them
                cls()
                if playerChoice == "exit" or computerChoice == "exit":
                    print("Leaving...")
                    break
                elif playerChoice.isdigit() and computerChoice.isdigit():
                    roundWinner = rspCheckResult(player1, player2, int(playerChoice), int(computerChoice))
                    
                    if roundWinner == 1:
                        print(player1, "chose", choicesGet(playerChoice), ",", player2, "chose", choicesGet(computerChoice), ":", player1, "won the round!")
                        playerScore += 1
                    elif roundWinner == 2:
                        print(player1, "chose", choicesGet(playerChoice), ",", player2, "chose", choicesGet(computerChoice), ":", player2, "won the round!")                      
                        computerScore += 1
                    
                else:
                    print("Invalid input")
                
                
            print("\nWinner: ", player1 if playerScore > computerScore else player2)
            if input("\nDo you want to play again? (1: Yes, Anything else: No): ") == "1":
                computerScore = 0
                playerScore = 0
                continue
            else: break
        
    elif MenuChoice == "mind reader" or MenuChoice == "2":
        '''Mind Reader Code'''
        cls()
        while True:
            print("\nWelcome to Mind Reader!\n")
            while True:
                try:
                    diff = int(input("Difficulty 1: 1-10\nDifficulty 2: 1-20\nDifficulty 3: 1-30\nPlease select a difficulty (1-3): "))
                    if diff <= 3 and diff >= 1:
                        break
                    else:
                        print("Too high or too low")
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
        

    elif MenuChoice == "optimus prime" or MenuChoice == "3":
        '''Optimus Prime Code'''        
        while True:
            cls()
            print("***************************\nWelcome to Optimus Prime\n***************************")
            print("Here I check if the number you will insert is a prime number or not\n\nPlease input any number, no decimals nor negatives!")
            while True:
                userInput = input("(exit to leave) Number: ")
                if userInput == "exit":
                    break
                elif userInput.isdigit() and int(userInput) > 1:
                    checkPrime(int(userInput))
                else:
                    print("InputError!")
                    
            if input("\nDo you want to test another number? (1: Yes, Anything else: No): ") == "1":
                continue
            else: break 
        
    elif MenuChoice == "tutorial" or MenuChoice == "4":
        '''Tutorial Code'''
        while True:
            cls()
            print("\n********\nTutorial\n********")
            print("Most places uses numbers 1-3 as input, some how big of a a number you'd like.\nType 'exit' almost anywhere to either go back or exit the whole game")
            if input("'exit' for main menu: ") == "exit":
                break
            else:
                print("input error")

    
    else:
        print("Please type one of the above!")