import numpy as np
import matplotlib.pyplot as plt


# ============================================
# SAMPLE FORCE-POSITION DATA
# ============================================

# Position (meters)
x = np.array([
    0,
    1,
    2,
    3,
    4,
    5
])

# Force (Newtons)
F = np.array([
    0,
    2,
    5,
    4,
    3,
    0
])


# ============================================
# NUMERICAL INTEGRATION
# ============================================

# Trapezoidal Rule
work = np.trapz(F, x)


# ============================================
# DISPLAY RESULTS
# ============================================

print("================================")
print("WORK & POWER CALCULATOR")
print("================================")

print(f"Computed Work = {work:.4f} Joules")


# ============================================
# OPTIONAL POWER CALCULATION
# ============================================

velocity = 2.0  # m/s

# Instantaneous power at each point
power = F * velocity

print(f"\nVelocity = {velocity} m/s")

print("\nPower Values:")

for i in range(len(power)):
    print(
        f"x = {x[i]:.1f} m "
        f"| P = {power[i]:.2f} W"
    )


# ============================================
# FORCE vs POSITION PLOT
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    x,
    F,
    marker='o'
)

plt.fill_between(
    x,
    F,
    alpha=0.3
)

plt.xlabel("Position (m)")
plt.ylabel("Force (N)")

plt.title("Force vs Position")

plt.grid(True)

plt.show()


# ============================================
# POWER vs POSITION PLOT
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(
    x,
    power,
    marker='o'
)

plt.xlabel("Position (m)")
plt.ylabel("Power (W)")

plt.title("Power vs Position")

plt.grid(True)

plt.show()