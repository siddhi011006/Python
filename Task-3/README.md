# Task 3: Control Flow, Functions & Menu-Driven Applications

This directory contains the solutions, traces, and implementations for Task 3, covering while loops, state management across menu choices, input validation, binary search algorithms, and modular program design.

---

## Section A: Concept Check

1. When a menu-driven program needs to remember something across multiple choices in the same run (for example, an account balance), that value must be stored **outside (before)** the main loop, not inside it.  
   *(If stored inside, the value gets re-initialized back to its starting state on every new iteration).*
2. To generate a random number in Python, you first need to **import** the `random` module.
3. In a "computer guesses your number" game, the computer narrows its guesses using feedback from the user, which is the same principle as a **binary** search.
4. If a withdrawal amount in an ATM simulation exceeds the current balance, the correct response is to **reject (cancel)** the transaction and print an error, not to allow a negative balance.
5. A `while` loop condition that depends on a variable changed inside the loop (like attempts or balance) will only terminate if that variable is **updated** correctly on every iteration.

---

## Section B: Logic Traces

### 1. ATM Simulation Trace
- **Initial Balance:** Rs. 5000.00
- **Step 1: Check Balance**  
  - Current balance displayed: **Rs. 5000.00**
- **Step 2: Withdraw 2000**  
  - Check: `2000 <= 5000` (Valid)
  - Calculation: `5000 - 2000 = 3000`
  - Balance after operation: **Rs. 3000.00**
- **Step 3: Deposit 500**  
  - Calculation: `3000 + 500 = 3500`
  - Balance after operation: **Rs. 3500.00**
- **Step 4: Withdraw 4000**  
  - Check: `4000 <= 3500` (False)
  - **Result:** **Transaction Rejected!** Insufficient funds. The withdrawal is cancelled and no money is deducted.
  - Final Balance remains: **Rs. 3500.00**

---

### 2. Reverse Guessing Game Trace (Range 1 to 100, Secret Number = 37)
The computer picks the midpoint `mid = (low + high) // 2` at every turn:
- **Guess 1:** Range `[1, 100]`  
  - Midpoint: `(1 + 100) // 2 = 50`  
  - User feedback: **Too High** (since 37 < 50)  
  - New Range: `[1, 49]`
- **Guess 2:** Range `[1, 49]`  
  - Midpoint: `(1 + 49) // 2 = 25`  
  - User feedback: **Too Low** (since 37 > 25)  
  - New Range: `[26, 49]`
- **Guess 3:** Range `[26, 49]`  
  - Midpoint: `(26 + 49) // 2 = 37`  
  - User feedback: **Correct!**  
  - The secret number 37 is found in **3 guesses**.

---

### 3. Student Grade Calculation Trace
- **Subject Marks:** 85, 92, 78, 60, 55
- **Sum of Marks:** `85 + 92 + 78 + 60 + 55 = 370`
- **Average:** `370 / 5 = 74.0%`
- **Grade Assignment:**
  - `90 and above`: A
  - `75 to 89`: B
  - `60 to 74`: C
  - `40 to 59`: D
  - `below 40`: F
- Since 74.0 falls in the range `60 to 74`, the assigned grade is **C**.

---

## Section C & E: Programs & Documentation

### Program 1: ATM Simulation (`atm_simulation.py`)
- **Aim:** Simulates an interactive ATM allowing balance inquiries, deposits, withdrawals with overdraft protection, and PIN management.
- **Logic:** State variables (`balance`, `pin`) are declared outside the main `while` loop so changes persist across transactions. Each withdrawal request verifies that the amount does not exceed the current balance before deduction occurs.
- **Sample Run (Testing PIN, transactions, and rejected overdraft):**
  ```text
  Please enter your 4-digit PIN: 1234
  PIN verified successfully!

  ------------- ATM MENU -------------
  1. Check Balance
  2. Deposit Funds
  3. Withdraw Funds
  4. Change PIN
  5. Exit
  ------------------------------------
  Enter your choice (1-5): 1
  >> Your Current Balance is: Rs. 5000.00

  Enter your choice (1-5): 3
  Enter amount to withdraw: Rs. 2000
  >> Success: Please collect Rs. 2000.00.
  >> Remaining Balance: Rs. 3000.00

  Enter your choice (1-5): 2
  Enter amount to deposit: Rs. 500
  >> Success: Rs. 500.00 deposited.
  >> New Balance: Rs. 3500.00

  Enter your choice (1-5): 3
  Enter amount to withdraw: Rs. 4000
  >> Transaction Rejected: Insufficient balance.
  >> Attempted: Rs. 4000.00 | Available: Rs. 3500.00

  Enter your choice (1-5): 5
  >> Thank you for banking with us. Goodbye!
  ```

---

### Program 2: Student Grade Calculator (`grade_calculator.py`)
- **Aim:** Calculates a student's average across 5 subjects, assigns a letter grade, and retains the record to view anytime via the menu.
- **Logic:** Storing the `last_student` dictionary outside the menu loop allows Option 2 to display the latest saved report. Grade boundaries are evaluated using standard chained `if-elif-else` conditionals.
- **Sample Run (Testing empty record check, entry, and view report):**
  ```text
  ------------- GRADE MENU -------------
  1. Enter marks for a new student
  2. View grade of last entered student
  3. Exit
  --------------------------------------
  Enter your choice (1-3): 2
  >> No student record found yet. Please choose option 1 to enter marks first.

  Enter your choice (1-3): 1
  Enter student name: Siddhi
  Enter marks for 5 subjects (0 to 100):
    Subject 1 mark: 85
    Subject 2 mark: 92
    Subject 3 mark: 78
    Subject 4 mark: 60
    Subject 5 mark: 55

  >> Student record saved successfully!
  >> Name: Siddhi | Average: 74.00 | Grade: C

  Enter your choice (1-3): 2

  ------------- LAST STUDENT REPORT -------------
  Name   : Siddhi
  Marks  : 85.0, 92.0, 78.0, 60.0, 55.0
  Total  : 370.00 / 500
  Average: 74.00%
  Grade  : C
  -----------------------------------------------
  ```

---

### Program 3: Reverse Guessing Game (`reverse_guessing_game.py`)
- **Aim:** Allows the user to think of a secret number within a custom range while the computer guesses it using binary search.
- **Logic:** The search space is bounded by `low` and `high`. The computer always guesses the midpoint `(low + high) // 2`. User feedback (`H`, `L`, `C`) shifts either `high = guess - 1` or `low = guess + 1`, cutting the search range in half each round.
- **Sample Run (Testing range 1-100 with secret number 37):**
  ```text
  Enter the lower bound of your range (e.g., 1): 1
  Enter the upper bound of your range (e.g., 100): 100

  Keep your secret number between 1 and 100 in mind!
  Press [Enter] when you are ready...

  Attempt #1: Is your secret number 50?
  Feedback options: [H] Too High | [L] Too Low | [C] Correct
  Your feedback: H

  Attempt #2: Is your secret number 25?
  Feedback options: [H] Too High | [L] Too Low | [C] Correct
  Your feedback: L

  Attempt #3: Is your secret number 37?
  Feedback options: [H] Too High | [L] Too Low | [C] Correct
  Your feedback: C

  >> Woohoo! The computer found your number (37) in 3 guess(es)!
  ```

---

### Program 4: Guessing Game with Hints and Scoring (`guessing_game_hints.py`)
- **Aim:** A number guessing game where the player tries to guess the computer's randomly selected number with scoring and mathematical clues.
- **Logic:** The player starts with 100 points, losing 10 points for each incorrect guess. After each wrong attempt, the program calculates modulo operations (`% 2` for parity, `% 5` for divisibility) and relative comparison (`>` or `<`) to guide the user.
- **Sample Run:**
  ```text
  I have picked a secret number between 1 and 100.
  You start with 100 points. Each wrong guess deducts 10 points.
  You have a maximum of 10 attempts. Good luck!

  Attempt #1 (Attempts left: 10) - Enter guess: 50
  >> Wrong guess! The secret number is HIGHER than 50.
  >> [HINT]: The secret number is EVEN and is NOT a multiple of 5.
  >> Current Score: 90

  Attempt #2 (Attempts left: 9) - Enter guess: 82
  >> Congratulations! You guessed the secret number 82 correctly!
  >> Attempts taken: 2
  >> Final Score: 90 / 100
  ```

---

### Program 5: Combined Application (`combined_application.py`)
- **Aim:** Integrates the ATM Simulation, Student Grade Calculator, and Guessing Game into a unified multi-utility program with a top-level menu.
- **Logic:** Functions from the individual modules (`atm_app`, `grade_calculator_app`, `guessing_game_hints_app`) are imported and invoked based on the user's top-level selection. Each subprogram returns control to the master loop upon exit.
- **Sample Run:**
  ```text
  ========================================
            MULTI-UTILITY SUITE           
========================================
  1. ATM Simulation
  2. Student Grade Calculator
  3. Number Guessing Game (with Hints & Scoring)
  4. Exit Suite
  ========================================
  Select an application (1-4): 1

  [Enters ATM simulation... completes transactions... chooses Option 5 (Exit)]

  >> Thank you for banking with us. Goodbye!

  ========================================
            MULTI-UTILITY SUITE           
========================================
  1. ATM Simulation
  2. Student Grade Calculator
  3. Number Guessing Game (with Hints & Scoring)
  4. Exit Suite
  ========================================
  Select an application (1-4): 4

  >> Exiting Multi-Utility Suite. Have a great day!
  ```

---

## Section D: Analysis

### 1. Why Binary Search Guarantees Finding the Number in Far Fewer Guesses (1 to 100)
In linear search (guessing numbers one by one), each guess eliminates only one single number. In the worst case, checking 1 to 100 takes 100 guesses, with an average of 50 guesses.  
In contrast, binary search guesses the midpoint of the active range at every step. Because the user indicates whether the guess is too high or too low, **exactly half of all remaining possibilities are eliminated on every single iteration**. For a range of size $N = 100$:
- Guess 1 narrows 100 candidates to 50
- Guess 2 narrows 50 candidates to 25
- Guess 3 narrows 25 candidates to 12
- Guess 4 narrows 12 candidates to 6
- Guess 5 narrows 6 candidates to 3
- Guess 6 narrows 3 candidates to 1
- Guess 7 guarantees finding the number.

Mathematically, $\lceil \log_2(100) \rceil = 7$. Binary search guarantees finding any number between 1 and 100 in **at most 7 guesses**, compared to up to 100 for linear search.

---

### 2. The Bug if Balance Check Happened After Subtracting Instead of Before
If an ATM code executes:
```python
balance = balance - withdrawal
if balance < 0:
    print("Error: Insufficient balance")
```
The account balance in memory **has already become negative** before the error is handled. This creates severe real-world vulnerabilities:
1. If the program crashes, raises an exception, or terminates right after the subtraction, the account remains permanently overdrawn.
2. The developer would be forced to remember to manually write rollback code (`balance = balance + withdrawal`) in every error block, which is prone to omission.
3. In concurrent or multi-threaded banking systems, another transaction could read the negative balance in the split second before rollback occurs.

Checking `if withdrawal > balance` **before** performing the subtraction ensures that system state is only mutated when the transaction is valid.

---

### 3. How Parity and Divisibility Hints Change Expected Guesses
Yes, the parity (even/odd) and multiple-of-5 hints significantly reduce the expected number of guesses:
- Telling the user whether the number is **even or odd immediately eliminates 50% of the candidate numbers** in the current range.
- The **multiple-of-5 hint** further narrows the pool:
  - If it is a multiple of 5, 80% of the numbers in that range are eliminated immediately (only numbers ending in 0 or 5 remain).
  - If it is not a multiple of 5, the 20% of numbers that are multiples of 5 are eliminated.
- Combining both hints with the directional hint (higher/lower) restricts the search space far more rapidly than high/low alone. For instance, if the secret number is between 50 and 100, is ODD, and is a MULTIPLE OF 5, the only possible candidates are: 55, 65, 75, 85, and 95 (only 5 possibilities out of 50!). This cuts down the expected attempts substantially.

---

### 4. Returning Control to the Top-Level Menu in the Combined Application
In standalone console scripts, beginners often terminate the program on an "Exit" selection using `sys.exit()` or `quit()`. If `sys.exit()` were used inside individual subprograms, selecting "Exit" inside the ATM or Grade Calculator would terminate the entire Python process, closing the entire application.

To make them work inside the Combined Application:
1. Each subprogram is encapsulated inside its own dedicated function (`atm_app()`, `grade_calculator_app()`, `guessing_game_hints_app()`).
2. Inside each function's `while True` menu loop, selecting "Exit" triggers a simple `break` or `return` statement instead of terminating the process.
3. This allows the function call in `combined_application.py` to finish naturally, transferring control back to the master loop and re-rendering the top-level menu.
