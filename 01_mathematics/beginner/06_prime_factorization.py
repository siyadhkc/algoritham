def prime_factors(n):
    if n <= 1:
        return {}

    factors = {}

    # Handle factor 2 separately
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2

    # Check odd factors up to sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2

    # If remainder is prime
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


def format_factors(factors):
    return " × ".join(
        f"{p}^{e}" if e > 1 else str(p)
        for p, e in factors.items()
    )

n = 360

factors = prime_factors(n)
print(factors)
print(format_factors(factors))