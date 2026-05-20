import math

def circular_motion(m, v, r):

    # angular velocity
    omega = v / r

    # period
    T = (2 * math.pi * r) / v

    # centripetal force
    F = (m * v**2) / r

    print("\n🌀 Circular Motion Results\n")

    print(f"Angular Velocity (ω) : {omega:.2f} rad/s")
    print(f"Period (T)           : {T:.2f} s")
    print(f"Centripetal Force    : {F:.2f} N")


# INPUT
m = float(input("Enter mass (kg): "))
v = float(input("Enter velocity (m/s): "))
r = float(input("Enter radius (m): "))

circular_motion(m, v, r)