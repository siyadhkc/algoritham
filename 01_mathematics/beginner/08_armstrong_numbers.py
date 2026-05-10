def is_armstrong(n):
    if n < 0:
        return False

    # Count digits
    temp = n
    k = 0
    while temp > 0:
        temp //= 10
        k += 1

    # Special case for 0
    if n == 0:
        return True

    # Compute sum of digit^k
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** k
        temp //= 10

    return total == n

# Genrete all numbers

def armstrong_up_to(limit):
    result = []
    for i in range(limit + 1):
        if is_armstrong(i):
            result.append(i)
    return result

print(armstrong_up_to(1000))