import math

# Constants
c = 299_792_458  # speed of light (m/s)

# Mass of object (kg)
m = 1.0

# Speeds as fractions of c
speed_fractions = [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]

print(f"{'v/c':<10}{'Classical p':<20}{'Relativistic p':<20}")

for frac in speed_fractions:
    v = frac * c

    # Classical momentum
    p_classical = m * v

    # Lorentz factor
    gamma = 1 / math.sqrt(1 - (v**2 / c**2))

    # Relativistic momentum
    p_relativistic = gamma * m * v

    print(
        f"{frac:<10}"
        f"{p_classical:<20.2e}"
        f"{p_relativistic:<20.2e}"
    )

    