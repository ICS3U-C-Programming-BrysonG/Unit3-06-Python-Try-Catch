#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 10 22, 2026
# This program gets a number from the user and compares it to the
# randomly generated number and will tell the user if it is
# correct or incorrect

import random


def main():
    # This function uses a try statement
    # Generate random number
    randomNum = random.randint(1, 10)

    # Get the guessed number from the user
    guessed_number_as_string = input("Enter your guessed number (1-10): ")

    # Try and compare user guess to randomly generated number
    try:
        guessed_number_as_int = int(guessed_number_as_string)
        if guessed_number_as_int == randomNum:
            print("You guessed correctly!")
        else:
            print(
                "You guessed wrong, the correct answer is {}".format(
                    randomNum
                )
            )
    except:
        print("{} is not a valid integer".format(guessed_number_as_string))
    finally:
        print("Play again!")

if __name__ == "__main__":
    main()
