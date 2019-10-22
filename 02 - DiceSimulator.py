from random import randint
from time import sleep
#
# Made by Filiph Wallsten 2019-09-19
#
i = 0
k = 0
total_wins = 0
dice_numbers = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,

}
running = True

rounds = int(input('How many games do you want to play? (20 is max) '))
while running:
    dice_result = randint(1, 6)
    dice_numbers[dice_result] += 1
    player_dice = int(input('Select number 1-6 '))
    print('Dice rolling...')
    sleep(1)
    print('You rolled: ', player_dice)
    print('House rolled: ', dice_result)

    if dice_result == player_dice:
        print('Its a match! You win!')
        total_wins+=1
    else:
        print('Aw, better luck next time!')
    i+=1    
    if i == rounds:
        for x in dice_numbers:
            k+=1
            print('Dice landed on ', k, ' :', dice_numbers[x], 'times')
        print('Average of correct guesses ', total_wins/rounds)
        break


