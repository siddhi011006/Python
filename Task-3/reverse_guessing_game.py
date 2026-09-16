# Task 3 - Program 3: Reverse Guessing Game (Computer Guesses Your Number)
# Uses binary search to guess the user's secret number in the minimum number of attempts.


def reverse_guessing_app():
    """
    Runs the reverse guessing game where the computer guesses the user's secret number.
    Uses a binary search algorithm to narrow the search range based on user feedback.
    """
    print("\n========================================")
    print("        REVERSE GUESSING GAME           ")
    print("========================================")
    print("Think of a secret integer within a range of your choice.")
    print("The computer will try to guess it using a binary search strategy!\n")

    # Range input with validation
    while True:
        try:
            low = int(input("Enter the lower bound of your range (e.g., 1): "))
            high = int(input("Enter the upper bound of your range (e.g., 100): "))
            if low >= high:
                print(">> Upper bound must be strictly greater than lower bound. Try again.\n")
                continue
            break
        except ValueError:
            print(">> Please enter valid integers for the range.\n")

    print(f"\nKeep your secret number between {low} and {high} in mind!")
    input("Press [Enter] when you are ready...")

    guesses_count = 0

    while low <= high:
        # Binary search midpoint guess
        guess = (low + high) // 2
        guesses_count += 1

        print(f"\nAttempt #{guesses_count}: Is your secret number {guess}?")
        print("Feedback options: [H] Too High | [L] Too Low | [C] Correct")
        feedback = input("Your feedback: ").strip().upper()

        if feedback in ["C", "CORRECT"]:
            print(f"\n>> Woohoo! The computer found your number ({guess}) in {guesses_count} guess(es)!")
            return

        elif feedback in ["H", "HIGH", "TOO HIGH"]:
            # If guess is too high, the secret number must be strictly smaller
            high = guess - 1

        elif feedback in ["L", "LOW", "TOO LOW"]:
            # If guess is too low, the secret number must be strictly larger
            low = guess + 1

        else:
            print(">> Unrecognized response. Please enter H, L, or C.")
            guesses_count -= 1  # Don't count invalid input as a guess attempt

    # If low > high, the user gave contradictory hints
    print("\n>> Hmm, the search range is empty! It seems some hints were contradictory.")
    print(">> Please double check your feedback when playing next time.")


if __name__ == "__main__":
    reverse_guessing_app()
