from random import randint        
fNum = randint(0, 9)
sNum = randint(0, 9)
tNum = randint(0, 9)
winningNum = [fNum, sNum, tNum]
running = True

print("Welcome the California lottery. If you can guess the 3-digit you win the jackpot!")

while running:
    playerGuessInput = input("Enter your 3-digit guess: ")
    if len(str(playerGuessInput)) < 3:
        print("You have to enter 3-digits!")
    else:
        playerGuessList = list(map(int,str(playerGuessInput)))
        if playerGuessList == winningNum:
            print("Congratulations! You won!")
            break
        else:
            print("Better luck next time!")
        playAgain = input("Do you want to play again?")
        if playAgain == "y":
            continue
        else:
            break