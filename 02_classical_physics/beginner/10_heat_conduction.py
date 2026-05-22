import numpy as np
import matplotlib.pyplot as plt


# ============================================
# PARAMETERS
# ============================================

length = 1.0          # rod length (m)
nodes = 20            # number of grid points

T_left = 100          # left boundary temperature
T_right = 25          # right boundary temperature

iterations = 500


# ============================================
# GRID SPACING
# ============================================

dx = length / (nodes - 1)


# ============================================
# INITIAL TEMPERATURE ARRAY
# ============================================

T = np.zeros(nodes)

# Boundary conditions
T[0] = T_left
T[-1] = T_right


# ============================================
# INITIAL GUESS
# ============================================

for i in range(1, nodes - 1):
    T[i] = (
        T_left
        + (T_right - T_left)
        * i / (nodes - 1)
    )


# ============================================
# FINITE DIFFERENCE ITERATION
# ============================================

for _ in range(iterations):

    T_old = T.copy()

    for i in range(1, nodes - 1):

        T[i] = (
            T_old[i - 1]
            + T_old[i + 1]
        ) / 2


# ============================================
# POSITION ARRAY
# ============================================

x = np.linspace(0, length, nodes)


# ============================================
# OUTPUT
# ============================================

print("================================")
print("1D HEAT CONDUCTION")
print("================================")

print(f"Rod Length: {length} m")
print(f"Grid Points: {nodes}")

print(
    f"Boundary Temperatures: "
    f"{T_left}°C -> {T_right}°C"
)

print("\nTemperature Distribution:\n")

for i in range(nodes):

    print(
        f"x = {x[i]:.3f} m "
        f"| T = {T[i]:.3f} °C"
    )


# ============================================
# PLOT TEMPERATURE PROFILE
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    x,
    T,
    marker='o'
)

plt.xlabel("Position Along Rod (m)")
plt.ylabel("Temperature (°C)")

plt.title("Steady-State Temperature Profile")

plt.grid(True)

plt.show()