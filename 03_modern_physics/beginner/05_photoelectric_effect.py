# the formula is Kmax​=hf−ϕ
# where h=6.626×10−34 J·s (Planck's constant)
# f = photon frequency(Hz)
# ϕ = work function 

h = 66.626e-34

# input
frequency  = float(input("Enter photon frequency (Hz): "))
work_function = float(input("Enter work function (J): "))

photon_energy = h * frequency 
kinetic_energy = photon_energy - work_function

if kinetic_energy > 0 :
    print(f"\nPhoton Energy : {photon_energy:.3e} J")
    print(f"Maximum Kinetic Energy :{kinetic_energy:.3e} J")
else:
    print("\nNo photoelectric emission occurs.")
    print(f"Photon Energy : {photon_energy:.3e} J")