# Task 4: Time and Space Complexity Analysis Snippets


# Snippet 1
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


# Snippet 2
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


# Snippet 3
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


# Snippet 4
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result


# Snippet 5
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


# Snippet 6
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


# Snippet 7
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples


# Snippet 8
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])


# Snippet 9
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False


# Snippet 10
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr


# Snippet 11
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# Snippet 12
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Snippet 13
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Snippet 14
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count


# Snippet 15
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)


# Snippet 16
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


# Snippet 17
def is_palindrome(s):
    return s == s[::-1]


# Snippet 18
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat


# Snippet 19
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


# Snippet 20
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


# Snippet 21
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False


# Snippet 22
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq
