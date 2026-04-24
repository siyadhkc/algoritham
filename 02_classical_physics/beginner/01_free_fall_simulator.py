# Subject : Physics
# Level   : Beginner
# Problem : Compute height, velocity and time for an object dropped from altitude H, ignoring drag.
# Concept : Kinematics equations 


# SIMPLE WAY 
# def free_fall(H):
#     g = 9.81
#     t = 0

#     while True:
#         h = H - 0.5 * g * t**2
#         v = g * t

#         print(t, h, v)

#         if h <= 0:
#             break

#         t += 1
# free_fall(100)
# ADVANCED WAY its like wow
import math

def free_fall(H):
    g = 9.81
    t_max = math.sqrt(2 * H / g)

    t = 0
    step = 1

    while t <= t_max:
        h = H - 0.5 * g * t**2
        v = g * t

        print(f"t={t}s | h={h:.2f}m | v={v:.2f}m/s")

        t += step

    # exact final state
    print(f"\nImpact at t={t_max:.2f}s with velocity={g*t_max:.2f}m/s")

H = float(input("Enter height (meters): "))
free_fall(H)

def simulate(H):
    g = 9.81
    v = 0
    h = H
    dt = 0.1
    t = 0

    while h > 0:
        v += g * dt
        h -= v * dt

        print(f"t={t:.2f} h={h:.2f} v={v:.2f}")

        t += dt