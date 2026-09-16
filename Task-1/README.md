# Task 1: Pattern Printing

This folder contains the solutions for the first lab assignment on nested loops and conditional statements in Python. Both questions are implemented in a single script (`task1.py`).

---

## Questions Overview

### 1. Hollow Diamond Pattern
- Takes an odd number `n` from the user.
- Prints a hollow diamond shape of stars (`*`).
- **Approach:** 
  - Instead of writing separate loops for the top and bottom halves, the program calculates the distance of the current row from the center: `d = abs(n // 2 - row)`.
  - The number of outer spaces equals `d`.
  - The number of inner spaces between stars equals `(n // 2 - d) * 2 - 1`.
  - The top and bottom tips only print a single star, while the middle rows print two stars separated by inner spaces.

### 2. Butterfly Pattern
- Takes a positive integer `n` from the user representing the half-size.
- Prints a symmetric butterfly star pattern with stars on the left and right wings, and spaces in the middle.
- **Approach:**
  - Divided into an upper (increasing) section from row `1` to `n` and a lower (decreasing) section from row `n - 1` down to `1`.
  - In each row, nested loops control the left stars, the middle spaces (`2 * (n - row)`), and the right stars.

---

## File Structure

- `task1.py`: Contains the complete source code for both questions along with an interactive menu.

---

## How to Run

Run the script from your terminal:

```bash
python task1.py
```

*(or `py task1.py` on Windows)*

Follow the on-screen prompts to enter values for each question.

---

## Sample Runs

### Run 1: Diamond (n = 7), Butterfly (n = 5)

**Input:**
```
Diamond size: 7
Butterfly rows: 5
```

**Output:**
```
Hollow Diamond:
   *
  * *
 *   *
*     *
 *   *
  * *
   *

Butterfly Pattern:
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

---

### Run 2: Diamond (n = 5), Butterfly (n = 3)

**Input:**
```
Diamond size: 5
Butterfly rows: 3
```

**Output:**
```
Hollow Diamond:
  *
 * *
*   *
 * *
  *

Butterfly Pattern:
*    *
**  **
******
**  **
*    *
```
