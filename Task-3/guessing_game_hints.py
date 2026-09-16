# Task 3 - Program 4: Guessing Game with Hints and Scoring
# Computer picks a secret random number, awards/deducts points, and gives mathematical hints.

import random


def guessing_game_hints_app():
    """
    Runs the guessing game where the user guesses the computer's secret number.
    Features:
    - 100 initial points (-10 per wrong guess)
    - Hints on parity (even/odd) and divisibility by 5
    - Maximum attempt limit
    """
    low_bound = 1
    high_bound = 100
    secret_number = random.randint(low_bound, high_bound)

    max_attempts = 10
    attempts_used = 0
    score = 100

    print("\n========================================")
    print("      NUMBER GUESSING GAME WITH HINTS   ")
    print("========================================")
    print(f"I have picked a secret number between {low_bound} and {high_bound}.")
    print(f"You start with {score} points. Each wrong guess deducts 10 points.")
    print(f"You have a maximum of {max_attempts} attempts. Good luck!\n")

    while attempts_used < max_attempts:
        attempts_used += 1
        remaining_attempts = max_attempts - attempts_used + 1

        try:
            guess = int(input(f"Attempt #{attempts_used} (Attempts left: {remaining_attempts}) - Enter guess: "))
        except ValueError:
            print(">> Invalid input! Please enter a whole integer.")
            attempts_used -= 1
            continue

        if guess == secret_number:
            print(f"\n>> Congratulations! You guessed the secret number {secret_number} correctly!")
            print(f">> Attempts taken: {attempts_used}")
            print(f">> Final Score: {score} / 100\n")
            return

        # Wrong guess handling
        score = max(0, score - 10)

        if attempts_used < max_attempts:
            direction = "HIGHER" if secret_number > guess else "LOWER"
            parity = "EVEN" if secret_number % 2 == 0 else "ODD"
            div_by_5 = "IS a multiple of 5" if secret_number % 5 == 0 else "is NOT a multiple of 5"

            print(f">> Wrong guess! The secret number is {direction} than {guess}.")
            print(f">> [HINT]: The secret number is {parity} and {div_by_5}.")
            print(f">> Current Score: {score}\n")

    # If loop completes without guessing correctly
    print("\n>> GAME OVER! You have used all your attempts.")
    print(f">> The secret number was: {secret_number}")
    print(">> Final Score: 0 / 100\n")


if __name__ == "__main__":
    guessing_game_hints_app()
