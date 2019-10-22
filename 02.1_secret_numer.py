from random import randint
from time import sleep

num_secret = randint(1, 100)
challenge_mode = randint(1, 10)
running = True
unlimited = False

unlimited_tries = input("Do you want unlimited tries? Enter 'y' or 'n' ")
if unlimited_tries == "y":
    unlimited = True

while running:
    if unlimited_tries == "y":
        num_guess = int(input("Enter a number in the range of 1-100 "))
        print(num_guess)
        if num_guess < num_secret:
            print (num_guess, " is less than the secret number")
        elif num_guess > num_secret:
            print (num_guess, " is bigger than the secret number")
        if num_guess == num_secret:
            print("CONGRATULATIONS! ITS A MATCH")
            break
    if unlimited_tries == "n":
        print("You got ", challenge_mode, "chances to guess right" )
        num_guess = int(input("Enter a number in the range of 1-100 "))
        
        if num_guess < num_secret:
            print (num_guess, " is less than the secret number")
            challenge_mode = challenge_mode - 1
        elif num_guess > num_secret:
            print (num_guess, " is bigger than the secret number")
            challenge_mode = challenge_mode - 1
        if num_guess == num_secret:
            print("CONGRATULATIONS! ITS A MATCH")
            break

  

