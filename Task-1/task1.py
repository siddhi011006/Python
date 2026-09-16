# Task 1: Pattern Printing Lab Assignment
# Question 1: Hollow Diamond Pattern
# Question 2: Butterfly Pattern


def hollow_diamond(n):
    """
    Prints a hollow diamond pattern for an odd integer n using nested loops.
    """
    mid = n // 2

    for i in range(n):
        # Distance from the center row
        d = abs(mid - i)
        outer_spaces = d
        inner_spaces = (mid - d) * 2 - 1

        # Print leading spaces
        for s in range(outer_spaces):
            print(" ", end="")

        # Print the first star
        print("*", end="")

        # Print middle spaces and the second star (for all rows except tips)
        if inner_spaces >= 0:
            for s in range(inner_spaces):
                print(" ", end="")
            print("*", end="")

        print()


def butterfly_pattern(n):
    """
    Prints a butterfly pattern for a positive integer n using nested loops.
    Divided into an increasing section (upper half) and a decreasing section (lower half).
    """
    # Upper half (increasing section, rows 1 to n)
    for i in range(1, n + 1):
        # Left stars
        for j in range(i):
            print("*", end="")
        # Middle spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Right stars
        for j in range(i):
            print("*", end="")
        print()

    # Lower half (decreasing section, rows n-1 down to 1)
    for i in range(n - 1, 0, -1):
        # Left stars
        for j in range(i):
            print("*", end="")
        # Middle spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Right stars
        for j in range(i):
            print("*", end="")
        print()


def main():
    print("========================================")
    print("      Python Lab Task 1 - Patterns      ")
    print("========================================\n")

    # --- Question 1: Hollow Diamond ---
    print("--- Question 1: Hollow Diamond Pattern ---")
    while True:
        try:
            n1 = int(input("Enter an odd number for diamond size (e.g., 7): "))
            if n1 <= 0:
                print("Please enter a positive number.")
                continue
            if n1 % 2 == 0:
                print("Diamond pattern requires an odd number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("\nHollow Diamond:")
    hollow_diamond(n1)
    print()

    # --- Question 2: Butterfly Pattern ---
    print("--- Question 2: Butterfly Pattern ---")
    while True:
        try:
            n2 = int(input("Enter number of rows for butterfly pattern (e.g., 5): "))
            if n2 <= 0:
                print("Please enter a positive number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("\nButterfly Pattern:")
    butterfly_pattern(n2)
    print("\nTask completed successfully!")


if __name__ == "__main__":
    main()
