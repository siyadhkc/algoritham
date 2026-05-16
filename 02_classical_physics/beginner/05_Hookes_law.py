import numpy as np
import matplotlib.pyplot as plt


# ============================================
# PARAMETERS
# ============================================

m = 1.0          # mass (kg)
k = 4.0          # spring constant (N/m)

A = 1.0          # amplitude (m)
phi = 0          # phase

t_max = 20
dt = 0.01


# ============================================
# TIME ARRAY
# ============================================

t = np.arange(0, t_max, dt)


# ============================================
# ANGULAR FREQUENCY
# ============================================

omega = np.sqrt(k / m)


# ============================================
# POSITION
# ============================================

x = A * np.cos(omega * t + phi)


# ============================================
# VELOCITY
# ============================================

v = -A * omega * np.sin(omega * t + phi)


# ============================================
# ENERGIES
# ============================================

kinetic = 0.5 * m * v**2

potential = 0.5 * k * x**2

total = kinetic + potential


# ============================================
# PRINT INFO
# ============================================

print("================================")
print("HOOKE'S LAW SPRING SYSTEM")
print("================================")

print(f"Mass (m): {m} kg")
print(f"Spring Constant (k): {k} N/m")
print(f"Angular Frequency: {omega:.4f} rad/s")

period = 2 * np.pi / omega
print(f"Period: {period:.4f} s")


# ============================================
# POSITION PLOT
# ============================================

plt.figure(figsize=(10, 5))
plt.plot(t, x)

plt.xlabel("Time (s)")
plt.ylabel("Position x(t)")

plt.title("Mass-Spring Position")

plt.grid(True)
plt.show()


# ============================================
# VELOCITY PLOT
# ============================================

plt.figure(figsize=(10, 5))
plt.plot(t, v)

plt.xlabel("Time (s)")
plt.ylabel("Velocity v(t)")

plt.title("Mass-Spring Velocity")

plt.grid(True)
plt.show()


# ============================================
# ENERGY PLOT
# ============================================

plt.figure(figsize=(10, 5))

plt.plot(t, kinetic, label="Kinetic Energy")
plt.plot(t, potential, label="Potential Energy")
plt.plot(t, total, label="Total Energy")

plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")

plt.title("Energy Conservation")

plt.legend()
plt.grid(True)

plt.show()