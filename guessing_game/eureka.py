#!/usr/bin/python3

import random

num = random.randint(1, 100)
past_guess = []

print()
print("Welcome to the Enigma_Explorer", end="\n")
Name = input("Enter Your User Name: ")


print()
print("Hello {}, This is The Guessing Number Challenge.". format(Name))
print("The Rules are as follows")
print("-" * 80)
print("""1. A random number has been generated, you are to take
      a guess of any number from 1 - 100"""
      )
print("""2. If your guess isn't the same as the number, keep
      trying until you get the correct number"""
      )
print("3. Your input must be a number")
print()
print("-" * 80)
print()

while True:
    player_guess = int(input("Take a guess from 1 - 100: "))

    if player_guess == num:
        print()
        print("Eureka!! :-), You have guessed correct")
        print()
        print("{}, you guessed a total of {} times".format(Name, no_of_guesses))
        break

    if player_guess < 1 or player_guess > 100:
        print("OUT OF BOUNDS")
    if num - 10 <= player_guess <= num + 10:
        print("WARM")
    else:
        print("COLD")

    if player_guess != num:
        past_guess.append(player_guess)
    p_guess = past_guess[-1]

    new_guess = int(input("Try again : "))
    if abs(new_guess - num) < abs(p_guess - num):
        print("WARMER")
    elif abs(new_guess - num) == abs(p_guess - num):
        print("WARM")
    else:
        print("COLDER")
    no_of_guesses = len(past_guess)
