# 1. Factorial (Iterative — Correct Approach)
def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result
# 2. Permutations P(n,r)
def permutation(n, r):
    if not (0 <= r <= n):
        return 0

    result = 1
    for i in range(n, n - r, -1):
        result *= i

    return result
# 3. Combinations C(n,r)
# Efficient (Avoid full factorials)
def combination(n, r):
    if not (0 <= r <= n):
        return 0

    r = min(r, n - r)  # symmetry optimization

    numerator = 1
    denominator = 1

    for i in range(1, r + 1):
        numerator *= (n - i + 1)
        denominator *= i

    return numerator // denominator