import numpy as np
import matplotlib.pyplot as plt


# ============================================
# CONSTANT
# ============================================

c = 299792458  # speed of light (m/s)


# ============================================
# LORENTZ FACTOR
# ============================================

def lorentz_factor(v):

    if v >= c:
        raise ValueError(
            "Velocity must be less than speed of light."
        )

    gamma = 1 / np.sqrt(
        1 - (v**2 / c**2)
    )

    return gamma


# ============================================
# TIME DILATION
# ============================================

def time_dilation(t, velocity_fraction):

    v = velocity_fraction * c

    gamma = lorentz_factor(v)

    t_prime = t / gamma

    return t_prime, gamma


# ============================================
# EXAMPLE
# ============================================

t_earth = 10  # years

velocity_fraction = 0.9


# ============================================
# CALCULATE
# ============================================

t_moving, gamma = time_dilation(
    t_earth,
    velocity_fraction
)


# ============================================
# OUTPUT
# ============================================

print("================================")
print("TIME DILATION CALCULATOR")
print("================================")

print(
    f"Velocity = {velocity_fraction}c"
)

print(
    f"Lorentz Factor γ = {gamma:.5f}"
)

print(
    f"Earth Time = {t_earth:.3f} years"
)

print(
    f"Moving Observer Time = "
    f"{t_moving:.3f} years"
)


# ============================================
# PLOT TIME DILATION
# ============================================

fractions = np.linspace(0, 0.999, 1000)

gammas = []

for f in fractions:

    v = f * c

    g = lorentz_factor(v)

    gammas.append(g)


# ============================================
# PLOT
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    fractions,
    gammas
)

plt.xlabel("Velocity Fraction v/c")
plt.ylabel("Lorentz Factor γ")

plt.title("Relativistic Time Dilation")

plt.grid(True)

plt.show()