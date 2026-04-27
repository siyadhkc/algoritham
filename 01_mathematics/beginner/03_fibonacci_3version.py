# import time

# # =========================
# # 1. Naive Recursion (slow)
# # =========================
# def fib_recursive(n):
#     if n <= 1:
#         return n
#     return fib_recursive(n-1) + fib_recursive(n-2)


# # =========================
# # 2. Memoization (fast)
# # =========================
# memo = {}

# def fib_memo(n):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fib_memo(n-1) + fib_memo(n-2)
#     return memo[n]


# # =========================
# # 3. Iteration (fastest)
# # =========================
# def fib_iter(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a


# # =========================
# # TIMING FUNCTION
# # =========================
# def measure(func, n):
#     start = time.time()
#     result = func(n)
#     end = time.time()
#     return result, end - start


# # =========================
# # INPUT
# # =========================
# n = int(input("Enter n: "))

# print("\n--- RESULTS ---")

# # recursive (limit to small n)
# if n <= 35:
#     res, t = measure(fib_recursive, n)
#     print(f"Recursive   → {res} | time: {t:.6f}s")
# else:
#     print("Recursive   → skipped (too slow)")

# # memoized
# res, t = measure(fib_memo, n)
# print(f"Memoization → {res} | time: {t:.6f}s")

# # iterative
# res, t = measure(fib_iter, n)
# print(f"Iteration   → {res} | time: {t:.6f}s")
import time

# -------- YOUR VERSION (iteration + print) --------
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


# -------- recursive --------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# -------- memoization --------
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


# -------- timing --------
def measure(func, n):
    start = time.time()
    result = func(n)
    return result, time.time() - start


# -------- INPUT --------
n = int(input("Enter n: "))

# sequence
print("\nSequence:")
print(fibonacci(n))

# comparison
print("\nPerformance:")

if n <= 35:
    _, t = measure(fib_recursive, n)
    print(f"Recursive:   {t:.6f}s")
else:
    print("Recursive:   skipped")

_, t = measure(fib_memo, n)
print(f"Memoization: {t:.6f}s")

_, t = measure(lambda x: fibonacci(x)[-1], n)
print(f"Iteration:   {t:.6f}s")
