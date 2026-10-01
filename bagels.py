"""Module providing a random number"""
import random

print("="*50)
print()
print("Bagels, a deductive logic game.")
print("By Al Sweigart al@inventwithpython.com")
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("When I say:    That means:")
print("  Pico         One digit is correct but in the wrong position.")
print("  Fermi        One digit is correct and in the right position.")
print("  Bagels       No digit is correct.")
print("I have thought up a number.")
print("You have 10 guesses to get it.")
print()
print("="*50)

SECRET_NUMBER = str(random.randint(100, 999))
MAX_GUESS = 10
guess = 1

print(SECRET_NUMBER)

while guess <= MAX_GUESS:
    print(f"Guess #{guess}:")
    guessed_number = input(">")
    if guessed_number in SECRET_NUMBER:
        print("in")
    guess += 1
