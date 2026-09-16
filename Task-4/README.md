# Task 4: Time and Space Complexity Analysis

This folder contains the Big-O time and space complexity solutions and one-line justifications for all 22 code snippets.

---

### Snippet 1
```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(1)$
- **Justify:** A single loop traverses the array of size $n$ once, using only a single scalar variable `max_val`.

---

### Snippet 2
```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```
- **Time complexity:** $O(n^2)$
- **Space complexity:** $O(1)$
- **Justify:** Nested loops compare every pair of elements ($\frac{n(n-1)}{2}$ comparisons in worst case) without allocating auxiliary data structures.

---

### Snippet 3
```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```
- **Time complexity:** $O(\log_{10} n)$
- **Space complexity:** $O(\log_{10} n)$
- **Justify:** The input $n$ is divided by 10 on each recursive step, producing a call stack depth equal to the number of digits ($\lfloor \log_{10} n \rfloor + 1$).

---

### Snippet 4
```python
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result
```
- **Time complexity:** $O(n^2)$
- **Space complexity:** $O(n^2)$
- **Justify:** Two nested loops execute $n \times n = n^2$ times, generating and storing all $n^2$ pairs in the `result` list.

---

### Snippet 5
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
- **Time complexity:** $O(\log n)$
- **Space complexity:** $O(1)$
- **Justify:** The search interval is cut in half on each loop iteration, using only a few constant tracking variables (`low`, `high`, `mid`).

---

### Snippet 6
```python
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result
```
- **Time complexity:** $O(n^3)$
- **Space complexity:** $O(n^2)$
- **Justify:** Three nested loops each iterate $n$ times ($n \times n \times n = n^3$ steps), and an $n \times n$ matrix is created to hold the product.

---

### Snippet 7
```python
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples
```
- **Time complexity (in terms of matrix dimensions m and n):** $O(m \cdot n)$
- **Space complexity (in terms of k non-zero elements):** $O(k)$
- **Justify:** It iterates over all $m \times n$ matrix cells once, storing only the $k$ non-zero entries as tuples in the list.

---

### Snippet 8
```python
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])
```
- **Time complexity:** $O(n^2)$
- **Space complexity:** $O(1)$
- **Justify:** The total work is $n + n^2$ operations, where the quadratic nested loop $O(n^2)$ dominates, while no extra memory is allocated.

---

### Snippet 9
```python
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(1)$
- **Justify:** The inner loop runs a fixed 10 times for each element ($10n$ operations), which is strictly linear $O(n)$ with $O(1)$ extra space.

---

### Snippet 10
```python
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(n)$
- **Justify:** A single loop visits all $n$ items in reverse order, appending each element into a newly created list of size $n$.

---

### Snippet 11
```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(1)$
- **Justify:** Two pointers iterate inward performing $n/2$ element swaps directly inside the existing array with zero extra allocated memory.

---

### Snippet 12
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(n)$
- **Justify:** The function makes $n$ linear recursive calls, producing a call stack depth of $n$ frames.

---

### Snippet 13
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```
- **Time complexity:** $O(2^n)$
- **Space complexity:** $O(n)$
- **Justify:** Each non-base call branches into two recursive calls forming an exponential recursion tree ($O(2^n)$ work), reaching a maximum stack depth of $n$.

---

### Snippet 14
```python
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(n)$
- **Justify:** Iterates through $n$ elements once with $O(1)$ average hash set lookups and insertions, storing up to $n$ elements in the `seen` set.

---

### Snippet 15
```python
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)
```
- **Time complexity:** $O(n \cdot 2^n)$
- **Space complexity:** $O(n)$
- **Justify:** The outer loop generates $2^n$ subsets and the inner bitwise loop runs $n$ times per subset, while the temporary list holds at most $n$ items.

---

### Snippet 16
```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```
- **Time complexity:** $O(len(a) + len(b))$
- **Space complexity:** $O(len(a) + len(b))$
- **Justify:** Traverses each item in both lists once using two pointers, allocating a combined output list of length $len(a) + len(b)$.

---

### Snippet 17
```python
def is_palindrome(s):
    return s == s[::-1]
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(n)$
- **Justify:** Slicing `s[::-1]` creates a new reversed string of length $n$ in $O(n)$ time and memory, followed by an $O(n)$ string comparison.

---

### Snippet 18
```python
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat
```
- **Time complexity (in terms of m rows and n columns):** $O(m \cdot n)$
- **Space complexity:** $O(m \cdot n)$
- **Justify:** Nested loops iterate through all $m$ rows and $n$ columns once, appending all $m \times n$ values into the new flat list.

---

### Snippet 19
```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```
- **Time complexity:** $O(exp)$
- **Space complexity:** $O(exp)$
- **Justify:** Recursion decrements `exp` by 1 until reaching 0, resulting in `exp` recursive calls and `exp` frames on the call stack.

---

### Snippet 20
```python
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base
```
- **Time complexity:** $O(\log(exp))$
- **Space complexity:** $O(\log(exp))$
- **Justify:** Dividing `exp` by 2 on each recursive step halves the exponent, using $\lfloor \log_2(exp) \rfloor + 1$ recursive calls and stack frames.

---

### Snippet 21
```python
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False
```
- **Time complexity (in terms of the sizes of a and b):** $O(|a| \cdot |b|)$
- **Space complexity:** $O(1)$
- **Justify:** Nested loops compare each element of `a` with each element of `b` ($|a| \times |b|$ steps in worst case) without allocating extra memory.

---

### Snippet 22
```python
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq
```
- **Time complexity:** $O(n)$
- **Space complexity:** $O(u)$ *(or $O(n)$ in worst case where all elements are unique)*
- **Justify:** Loops through $n$ elements with $O(1)$ average dictionary lookup and update, storing at most $n$ distinct key-value pairs.
