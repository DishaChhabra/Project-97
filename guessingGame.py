import random
number = random.randint(1,9)
chances = 0

while chances<5:
    chances = chances+1
    guess=int(input('enter your guess (1-9) : '))
    if guess==number:
        print('congratulations! you guessed right!')
        break
    elif guess>number:
        print('your guess is wrong, try a lower number than ',guess)
    elif guess<number:
        print('your guess is wrong, try a higher number than ',guess)
4
if chances==5:
    print('you lose! the number was ',number)