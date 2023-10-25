#!/usr/bin/python3

import random

def get_valid_guess():
    while True:
        try:
            guess = int(input("Take a guess from 1 - 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("OUT OF BOUNDS")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_guessing_game():
    num = random.randint(1, 100)
    past_guess = []
    no_of_guesses = 0

    print("\nWelcome to the Enigma_Explorer")
    Name = input("Enter Your User Name: ")

    print("\nHello {}, This is The Guessing Number Challenge.".format(Name))
    print("-" * 80)
    print("1. A random number has been generated, you are to take a guess of any number from 1 - 100")
    print("2. If your guess isn't the same as the number, keep trying until you get the correct number")
    print("3. Your input must be a number")
    print("-" * 80)

    while True:
        player_guess = get_valid_guess()
        no_of_guesses += 1

        if player_guess == num:
            print("\nEureka!! :-), You have guessed correct")
            print("{}, you guessed a total of {} times\n".format(Name, no_of_guesses))
            break

        if num - 10 <= player_guess <= num + 10:
            print("WARM")
        else:
            print("COLD")

        if len(past_guess) > 0:
            p_guess = past_guess[-1]
            new_guess = get_valid_guess()
            no_of_guesses += 1

            if abs(new_guess - num) < abs(p_guess - num):
                print("WARMER")
            else:
                print("COLDER")

        past_guess.append(player_guess)

if __name__ == "__main__":
    play_guessing_game()

