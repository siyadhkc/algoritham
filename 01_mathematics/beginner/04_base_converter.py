# Subject : Mathematics
# Level   : Beginner
# Problem : Convert any decimal integer to binary, octal and hexadecimal without built-ins
# Concept : Divsion algorthim
# Number representation
# Base systems (used in memory, networking, cryptography)
# Bit-level thinking (binary = foundation of everything)
# def convert_base(n, base):
#     digits = "0123456789ABCDEF"
    
#     if n == 0:
#         return "0"
    
#     result = ""
    
#     while n > 0:
#         remainder = n % base
#         result = digits[remainder] + result
#         n //= base
    
#     return result


# # INPUT
# num = int(input("Enter decimal number: "))

# print("Binary      :", convert_base(num, 2))
# print("Octal       :", convert_base(num, 8))
# print("Hexadecimal :", convert_base(num, 16))


# ADVANCED METHOd
import time

def convert_visual(n, base):
    digits = "0123456789ABCDEF"
    steps = []

    original = n

    while n > 0:
        steps.append((n, n % base))
        n //= base

    print(f"\n🧠 Converting {original} to base {base}:\n")

    result = ""
    for value, rem in steps:
        print(f"{value} ÷ {base} → remainder {rem}")
        result = digits[rem] + result
        time.sleep(0.5)

    print("\nResult:", result)


num = int(input("Enter number: "))
convert_visual(num, 2)
convert_visual(num, 8)
convert_visual(num, 16)