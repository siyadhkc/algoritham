#  in 1924 louis de Broglie proposed that every moving particle behaves like a wave this is called wave particle duality 
#  Formula is λ=p/h 
#  λ (lambda) = wavelength (meters)
#  h = planck's constant = 6.626 x 10 -34 js 
#  p = momentum
#  MOmentum is p = mv
import math

# Constants
PLANCK = 6.62607015e-34      # J·s
ELECTRON_MASS = 9.10938356e-31  # kg
PROTON_MASS = 1.6726219e-27     # kg
BASEBALL_MASS = 0.145           # kg (145 g)

# Particle masses
particles = {
    "electron": ELECTRON_MASS,
    "proton": PROTON_MASS,
    "baseball": BASEBALL_MASS
}

print("de Broglie Wavelength Calculator")
print("--------------------------------")

particle = input("Enter particle (electron/proton/baseball): ").lower()

if particle not in particles:
    print("Invalid particle!")
    exit()

ke = float(input("Enter kinetic energy (J): "))

mass = particles[particle]

# Momentum
momentum = math.sqrt(2 * mass * ke)

# de Broglie wavelength
wavelength = PLANCK / momentum

print(f"\nParticle : {particle.capitalize()}")
print(f"Kinetic Energy : {ke:.3e} J")
print(f"de Broglie Wavelength = {wavelength:.3e} m")