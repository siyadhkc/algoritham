import numpy as np


# ============================================
# INPUT PARAMETERS
# ============================================

mass = 10.0          # kg
angle_deg = 30       # degrees
mu = 0.2             # friction coefficient

g = 9.81             # m/s^2


# ============================================
# CONVERT ANGLE
# ============================================

theta = np.radians(angle_deg)


# ============================================
# GRAVITY
# ============================================

Fg = mass * g


# ============================================
# FORCE COMPONENTS
# ============================================

F_parallel = mass * g * np.sin(theta)

F_perpendicular = mass * g * np.cos(theta)


# ============================================
# NORMAL FORCE
# ============================================

N = F_perpendicular


# ============================================
# FRICTION FORCE
# ============================================

friction = mu * N


# ============================================
# ACCELERATION WITHOUT FRICTION
# ============================================

a_no_friction = g * np.sin(theta)


# ============================================
# ACCELERATION WITH FRICTION
# ============================================

a_with_friction = (
    g * (
        np.sin(theta)
        - mu * np.cos(theta)
    )
)


# ============================================
# OUTPUT
# ============================================

print("================================")
print("INCLINED PLANE SOLVER")
print("================================")

print(f"Mass: {mass} kg")
print(f"Angle: {angle_deg} degrees")
print(f"Friction coefficient: {mu}")

print("\n================================")
print("FORCES")
print("================================")

print(f"Gravity Force: {Fg:.3f} N")

print(
    f"Parallel Component: "
    f"{F_parallel:.3f} N"
)

print(
    f"Perpendicular Component: "
    f"{F_perpendicular:.3f} N"
)

print(f"Normal Force: {N:.3f} N")

print(f"Friction Force: {friction:.3f} N")


print("\n================================")
print("ACCELERATIONS")
print("================================")

print(
    f"Without Friction: "
    f"{a_no_friction:.3f} m/s²"
)

print(
    f"With Friction: "
    f"{a_with_friction:.3f} m/s²"
)