""" Number guessing game:
player will input a number to guess which number the app is asking

functions needed:
number generator
player input
app responds if its to low or too high
number of tries

"""
import random

random_number = random.randint(1, 100)


def guess_the_number():
    tries = 0
    while tries < 6:
        guess = int(input("What number is this? "))
        if guess > random_number:
            print('Guess High!')
            tries = tries + 1
        elif guess < random_number:
            print('Guess Low!')
            tries = tries + 1

        if guess == random_number:
            print("Guess is right!")
            print("Congratulations!")
            break
        elif tries < 5:
            print("Guess again:")
        if tries == 5:
            break


print(random_number)
guess_the_number()
