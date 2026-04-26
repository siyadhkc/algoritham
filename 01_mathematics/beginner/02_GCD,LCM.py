# Subject : Mathematics
# Level   : Beginner
# Problem : Compute greatest common divisor and LCM for two integers using the Euclidean algorithm.
# Concept : _Recursion / modulo_
# BUILT IN METHODE 
# import math

# a = int(input())
# b = int(input())

# print("GCD:", math.gcd(a, b))
# print("LCM:", abs(a*b) // math.gcd(a, b))

# def gcd(a,b):
#     while b != 0:
#         a, b = b,a%b
#     return abs(a)

# def lcm(a,b):
#     return abs(a*b)// gcd(a,b)
# a= int(input("Enter first number: "))
# b= int (input("Enter second number: "))

# print("GCD:", gcd(a,b))
# print("LCM:", lcm(a,b))


# ANimated Verssion 
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def gcd_visual(a, b):
    step = 1
    while b != 0:
        clear()
        print("🧠 Euclidean Algorithm Visualization\n")
        print(f"Step {step}:")
        print(f"GCD({a}, {b})")

        print("\nProcess:")
        print(f"{a} % {b} = {a % b}")

        time.sleep(1.2)

        a, b = b, a % b
        step += 1

    clear()
    print("✅ FINAL RESULT\n")
    print(f"GCD = {abs(a)}")
    return abs(a)

def lcm(a, b, gcd_val):
    return abs(a * b) // gcd_val


# INPUT
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = gcd_visual(a, b)
print(f"LCM = {lcm(a, b, g)}")
