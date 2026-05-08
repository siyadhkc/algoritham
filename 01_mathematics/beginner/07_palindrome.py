def is_palindrome(n: int) -> bool:
    # negatives and numbers ending with 0 (except 0) are not palindromes
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    rev = 0
    while n > rev:
        rev = rev * 10 + (n % 10)  # append last digit
        n //= 10                   # drop last digit

    # even length: n == rev
    # odd length:  n == rev // 10 (middle digit ignored)
    return n == rev or n == rev // 10

# methode two

def is_palindrome_full(n: int) -> bool:
    if n < 0:
        return False

    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10

    return original == rev

tests = [121, -121, 10, 12321, 1231, 0]

for t in tests:
    print(t, is_palindrome(t))