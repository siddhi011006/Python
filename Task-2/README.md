# Task 2: Star Pattern & Matrix Operations

This folder contains the solutions for the second lab assignment. Both problems are written in `task2.py` without using external libraries like NumPy, following standard Python lists and loop constructs.

---

## Questions Overview

### 1. Right-Angled Star Pattern
- Takes a positive integer `n` from the user.
- Prints a right-angled triangle pattern of asterisks where row `i` contains `i` stars.
- **Approach:**
  - Outer loop iterates through row numbers from `1` to `n`.
  - Inner loop prints `*` `i` times on the same line, followed by a newline.

### 2. 3x3 Matrix Operations
- Takes user input to create a 3x3 matrix (entered row-by-row).
- Performs the following five operations purely with lists and loops (no NumPy):
  1. **Display Matrix:** Formats and prints the 3x3 grid with clean alignment.
  2. **Total Sum:** Iterates across all rows and columns using nested loops to accumulate the sum of all elements.
  3. **Main Diagonal Sum:** Sums the elements where row index equals column index (`matrix[i][i]`).
  4. **Min and Max Elements:** Finds the largest and smallest values by traversing the matrix.
  5. **Transpose:** Constructs and displays the transposed matrix by swapping rows and columns (`matrix[j][i]`).

---

## How to Run

Navigate to the task folder and run:

```bash
python task2.py
```

*(or `py task2.py` on Windows)*

---

## Sample Runs

### Run 1: n = 5, Sequential Matrix (1 to 9)

**Pattern Input:** `n = 5`

```
*
**
***
****
*****
```

**Matrix Input:**
```
Row 1: 1 2 3
Row 2: 4 5 6
Row 3: 7 8 9
```

**Results:**
```
1. Matrix in row-and-column form:
   1    2    3 
   4    5    6 
   7    8    9 

2. Sum of all elements: 45
3. Sum of main diagonal elements: 15
4. Largest element: 9
   Smallest element: 1

5. Transpose of the matrix:
   1    4    7 
   2    5    8 
   3    6    9 
```

---

### Run 2: n = 3, Mixed Matrix with Negatives

**Pattern Input:** `n = 3`

```
*
**
***
```

**Matrix Input:**
```
Row 1: 12 -4 7
Row 2: 0 15 3
Row 3: -8 2 9
```

**Results:**
```
1. Matrix in row-and-column form:
  12   -4    7 
   0   15    3 
  -8    2    9 

2. Sum of all elements: 36
3. Sum of main diagonal elements: 36
4. Largest element: 15
   Smallest element: -8

5. Transpose of the matrix:
  12    0   -8 
  -4   15    2 
   7    3    9 
```
