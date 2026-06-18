# this is the one of the most famous results in physics from Albert Einstein

# The equation is : 
# E = Energy (joules)
# m = Mass (kg)
# c = Speed of light (299,792,458 m/s)
# Physics Insight
# Because c2 is enormous:
# c 2 ≈8.98755179×10
# 16
# Even a tiny amount of mass contains a tremendous amount of energy.
# For example:
# 1kg
# contains:
# 8.99×10
# 16
# joules of energy.
# Speed of light (m/s)
c = 299_792_458

# Mass in kg 
m = 1.0

# Energy (Joules)
E = m * c**2

print(f"mass: {m} kg")
print(f"Energy: {E:.3e} J")

def mass_energy(mass_kg):
    c = 299_792_458
    JOULES_PER_MEGATON = 4.184e15

    energy_j = mass_kg * c**2
    energy_mt = energy_j / JOULES_PER_MEGATON

    return energy_j, energy_mt


# Example
energy_j, energy_mt = mass_energy(1)

print(f"Energy = {energy_j:.3e} J")
print(f"Megatons = {energy_mt:.2f}")