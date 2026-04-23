# Subject : Mathematics
# Level   : Beginner
# Problem : Generate all primes up to N using the Sieve of Eratosthenes.
# Concept : Loops & booleans


def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    # Step 1: Assume all numbers are prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Step 2: Start sieving
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples as non-prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Step 3: Extract primes
    primes = [i for i, val in enumerate(is_prime) if val]
    return primes


print (sieve_of_eratosthenes(30))

# def optimized_sieve(n):
#     if n < 2:
#         return []

#     is_prime = [True] * (n // 2)
#     is_prime[0] = False  # 1 is not prime

#     for i in range(1, int(n**0.5)//2 + 1):
#         if is_prime[i]:
#             p = 2*i + 1
#             for j in range((p*p)//2, n//2, p):
#                 is_prime[j] = False

#     primes = [2] + [2*i + 1 for i in range(1, n//2) if is_prime[i]]
#     return primes

# print(optimized_sieve(30))
# this is optimized varient 
