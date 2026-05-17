import numpy as np
import matplotlib.pyplot as plt


# ============================================
# MOMENTUM
# ============================================

def momentum(mass, velocity):
    return mass * velocity


# ============================================
# KINETIC ENERGY
# ============================================

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2


# ============================================
# ELASTIC COLLISION
# ============================================

def elastic_collision(m1, u1, m2, u2):

    v1 = (
        ((m1 - m2) * u1 + 2 * m2 * u2)
        / (m1 + m2)
    )

    v2 = (
        ((m2 - m1) * u2 + 2 * m1 * u1)
        / (m1 + m2)
    )

    return v1, v2


# ============================================
# PERFECTLY INELASTIC COLLISION
# ============================================

def inelastic_collision(m1, u1, m2, u2):

    v = (
        (m1 * u1 + m2 * u2)
        / (m1 + m2)
    )

    return v


# ============================================
# VERIFY CONSERVATION
# ============================================

def verify_momentum(
    m1, u1,
    m2, u2,
    v1, v2
):

    initial = momentum(m1, u1) + momentum(m2, u2)

    final = momentum(m1, v1) + momentum(m2, v2)

    return initial, final


# ============================================
# EXAMPLE PARAMETERS
# ============================================

m1 = 2.0
u1 = 5.0

m2 = 3.0
u2 = -2.0


# ============================================
# ELASTIC COLLISION
# ============================================

v1, v2 = elastic_collision(
    m1, u1,
    m2, u2
)

print("================================")
print("ELASTIC COLLISION")
print("================================")

print(f"Object 1 Final Velocity: {v1:.3f} m/s")
print(f"Object 2 Final Velocity: {v2:.3f} m/s")


# ============================================
# MOMENTUM CHECK
# ============================================

p_initial, p_final = verify_momentum(
    m1, u1,
    m2, u2,
    v1, v2
)

print("\nMomentum Conservation:")
print(f"Initial Momentum = {p_initial:.3f}")
print(f"Final Momentum   = {p_final:.3f}")


# ============================================
# ENERGY CHECK
# ============================================

ke_initial = (
    kinetic_energy(m1, u1)
    + kinetic_energy(m2, u2)
)

ke_final = (
    kinetic_energy(m1, v1)
    + kinetic_energy(m2, v2)
)

print("\nKinetic Energy:")
print(f"Initial KE = {ke_initial:.3f} J")
print(f"Final KE   = {ke_final:.3f} J")


# ============================================
# PERFECTLY INELASTIC COLLISION
# ============================================

v_inelastic = inelastic_collision(
    m1, u1,
    m2, u2
)

print("\n================================")
print("PERFECTLY INELASTIC COLLISION")
print("================================")

print(f"Combined Final Velocity: {v_inelastic:.3f} m/s")


# ============================================
# INELASTIC MOMENTUM CHECK
# ============================================

p_initial_inelastic = (
    momentum(m1, u1)
    + momentum(m2, u2)
)

p_final_inelastic = (
    momentum(m1 + m2, v_inelastic)
)

print("\nMomentum Conservation:")
print(f"Initial Momentum = {p_initial_inelastic:.3f}")
print(f"Final Momentum   = {p_final_inelastic:.3f}")


# ============================================
# ENERGY LOSS
# ============================================

ke_final_inelastic = kinetic_energy(
    m1 + m2,
    v_inelastic
)

energy_loss = (
    ke_initial - ke_final_inelastic
)

print("\nEnergy Loss:")
print(f"Lost KE = {energy_loss:.3f} J")


# ============================================
# VISUALIZATION
# ============================================

labels = ["Initial", "Final"]

elastic_ke = [ke_initial, ke_final]

plt.figure(figsize=(8, 5))
plt.bar(labels, elastic_ke)

plt.ylabel("Kinetic Energy (J)")
plt.title("Elastic Collision Energy")

plt.grid(True)
plt.show()


inelastic_ke = [
    ke_initial,
    ke_final_inelastic
]

plt.figure(figsize=(8, 5))
plt.bar(labels, inelastic_ke)

plt.ylabel("Kinetic Energy (J)")
plt.title("Inelastic Collision Energy Loss")

plt.grid(True)
plt.show()