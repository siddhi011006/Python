# Task 2: Star Pattern & Matrix Operations Lab Assignment
# Question 1: Right-Angled Star Pattern
# Question 2: 3x3 Matrix Operations (Lists and Loops)


# ==========================================
# Question 1: Star Pattern
# ==========================================
def star_pattern(n):
    """
    Prints a right-angled star triangle of height n using nested loops.
    """
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()


# ==========================================
# Question 2: Matrix Operations
# ==========================================
def print_matrix(mat):
    """
    Displays a matrix in neat row-and-column format using nested loops.
    """
    for row in mat:
        for item in row:
            print(f"{item:4}", end=" ")
        print()


def matrix_operations(matrix):
    """
    Performs operations on a 3x3 matrix:
    1. Display matrix in row-column form
    2. Sum of all elements
    3. Sum of main diagonal elements
    4. Largest and smallest elements
    5. Transpose of the matrix
    """
    # 1. Display matrix
    print("\n1. Matrix in row-and-column form:")
    print_matrix(matrix)

    # 2. Sum of all elements
    total_sum = 0
    for row in matrix:
        for val in row:
            total_sum += val
    print(f"\n2. Sum of all elements: {total_sum}")

    # 3. Sum of main diagonal elements (row index == column index)
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += matrix[i][i]
    print(f"3. Sum of main diagonal elements: {diagonal_sum}")

    # 4. Largest and smallest elements
    largest = matrix[0][0]
    smallest = matrix[0][0]
    for row in matrix:
        for val in row:
            if val > largest:
                largest = val
            if val < smallest:
                smallest = val
    print(f"4. Largest element: {largest}")
    print(f"   Smallest element: {smallest}")

    # 5. Transpose of the matrix
    transpose = []
    for i in range(3):
        transposed_row = []
        for j in range(3):
            transposed_row.append(matrix[j][i])
        transpose.append(transposed_row)

    print("\n5. Transpose of the matrix:")
    print_matrix(transpose)


def main():
    print("========================================")
    print("      Python Lab Task 2                 ")
    print("========================================\n")

    # --- Question 1: Star Pattern ---
    print("--- Question 1: Star Pattern ---")
    while True:
        try:
            n = int(input("Enter the number of rows for star pattern (e.g., 5): "))
            if n <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nStar Pattern for n = {n}:")
    star_pattern(n)
    print()

    # --- Question 2: Matrix Operations ---
    print("--- Question 2: 3x3 Matrix Operations ---")
    print("Enter the elements for a 3x3 matrix row by row (space-separated):")

    matrix = []
    for i in range(3):
        while True:
            try:
                row_raw = input(f"Enter row {i + 1} (3 integers, e.g., 1 2 3): ").strip().split()
                if len(row_raw) != 3:
                    print("Please enter exactly 3 values separated by spaces.")
                    continue
                row = [int(x) for x in row_raw]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please make sure all values are integers.")

    matrix_operations(matrix)
    print("\nTask 2 completed successfully!")


if __name__ == "__main__":
    main()
