
from re import I
import random
from unittest import expectedFailure

'''RPS Variables'''
rpsChoices = [1,2,3]
playerScore = int(0)
computerScore = int(0)

'''Mind Reader Variables'''

'''Optimus Prime Variables'''

'''RSP Functions'''
def rspCheckResult(player, computer):
    roundWinner = 0
    if player in (rpsChoices):
        if player == computer:
            print("\nDraw!")
        elif player == 1 and computer == 2:
            print("\npPlayer 1 chose rock, player 2 chose scissors, player 1 won!")
            roundWinner = 1
        elif player == 1 and computer == 3:
            print("\nPlayer 1 chose rock, player 2 chose paper, player 2 won!")
            roundWinner = 2
        elif player == 2 and computer == 1: 
            print("\nPlayer 1 chose scissors, player 2 chose rock, player 2 won!")
            roundWinner = 2
        elif player == 2 and computer == 3:
            print("\nPlayer 1 chose scissors, player 2 chose paper, player 1 won!")
            roundWinner = 1
        elif player == 3 and computer == 1:
            print("\nPlayer 1 chose paper, player 2 chose rock, player 1 won!")
            roundWinner = 1
        elif player == 3 and computer == 2:
            print("\nPlayer 1 chose paper, player 2 chose scissors, player 2 won!")
            roundWinner = 2
    else:
        print("\nPlease choose between (1:Rock) (2:Scissors) (3:Paper)\n")
    return roundWinner
        
'''Mind Reader Functions'''

'''Optimus Prime Functions'''

'''Main Code'''
while True:
    print("\n**********\nMain Menu\n**********")
    MenuChoice = input("What do you want to play? :\nRPS, Mind Reader or Optimus Prime (no caps)\n")
    
    if MenuChoice == "exit":
        break
    
    elif MenuChoice == "rps":
        '''RPS Game Code'''
        
        while True:
            print("\nWelcome to RPS!\n")
            player1 = input("Player 1 name: \n")
            player2 = input("Player 2 name: (enter a zero if you want to play against computer) \n")
            if player2 == "0":
                player2 = "Computer"
            while True:
                try:
                    rounds = int(input("To how many points do you want to play?: "))
                    break
                except:
                    print("Not a number")
            
            while playerScore<rounds and computerScore<rounds:
                while True:
                    try:
                        playerChoice = int(input("Player 1 choose: \n1:Rock\n2:Scissors\n3:Paper\n"))
                        break
                    except:
                        print("Not a number")
                computerChoice = random.randint(1,3) if player2 == "Computer" else int(input("Player 2 choose: \n1:Rock\n2:Scissors\n3:Paper\n"))
                
                roundWinner = rspCheckResult(playerChoice, computerChoice)
                
                if roundWinner == 1:
                    playerScore += 1
                else:
                    computerScore += 1
                    
                print("\n",player1, ":", playerScore, "\n",player2,":",computerScore,"\n")
                
            print("Winner: ", player1 if playerScore > computerScore else player2)
            
            if input("Do you want to play again? (1: Yes, Anything else: No): ") == "1":
                computerScore = 0
                playerScore = 0
                continue
            else: break
        
    elif MenuChoice == "mind reader":
        '''Mind Reader Code'''
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

            while True:
                userGuess = input("Guess: ")
                if userGuess == "exit":
                    print("Leaving...")
                    break
                elif userGuess.isdigit():
                    if int(userGuess) == randNumber:
                        print("You chose wisely, well done!\nIt took you", guesses+1,"guess(es) to get it right.")
                        break
                    print("You need to go", 'higher' if int(userGuess) < randNumber else 'lower')
                    guesses += 1
                    print("Guesses:", guesses)
                else:
                    print("Incorrect input")
                
            if input("\nDo you want to play again (1: Yes, Anything else: No): ") == "1":
                continue
            else: break 
                
            
            # elif userGuess < randNumber:
            #     print("Too low fella!")
            # elif userGuess >
            
            # F'{oneTerm} + {twoTerm} ='
            
# >>> raining = False
# >>> print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the beach
# >>> raining = True
# >>> print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the library

# >>> age = 12
# >>> s = 'minor' if age < 21 else 'adult'
# >>> s
# 'minor'

# >>> 'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
# 'no'
            
            
            
        

    elif MenuChoice == "optimus prime":
        '''Optimus Prime Code'''        
        
    else:
        print("Please type one of the above!")