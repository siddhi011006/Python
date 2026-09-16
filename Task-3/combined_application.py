# Task 3 - Program 5: Combined Application
# Integrates ATM Simulation, Grade Calculator, and Guessing Game into a single master menu.

from atm_simulation import atm_app
from grade_calculator import grade_calculator_app
from guessing_game_hints import guessing_game_hints_app


def main():
    """
    Top-level menu controller that directs the user to individual modular applications.
    Returns control smoothly back to the top menu whenever a sub-application exits.
    """
    while True:
        print("\n========================================")
        print("          MULTI-UTILITY SUITE           ")
        print("========================================")
        print("1. ATM Simulation")
        print("2. Student Grade Calculator")
        print("3. Number Guessing Game (with Hints & Scoring)")
        print("4. Exit Suite")
        print("========================================")

        choice = input("Select an application (1-4): ").strip()

        if choice == "1":
            atm_app()

        elif choice == "2":
            grade_calculator_app()

        elif choice == "3":
            guessing_game_hints_app()

        elif choice == "4":
            print("\n>> Exiting Multi-Utility Suite. Have a great day!\n")
            break

        else:
            print(">> Invalid option! Please select a valid number from 1 to 4.\n")


if __name__ == "__main__":
    main()
