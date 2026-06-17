# about this formula 
# L′= contracted length (observed length)
# L = proper length (length in the object's rest frame)
# v = relative velocity
# c = speed of light (299,792,458 m/s)

# import math

# # Speed of light in m/s
# c = 299_792_458

# # Input values
# L = 10.0          # proper length (meters)
# v = 0.8 * c       # 80% of the speed of light

# # Compute Lorentz factor term
# factor = math.sqrt(1 - (v**2 / c**2))

# # Contracted length
# L_prime = L * factor
# print("Proper length:", L, "m")
# print("Velocity:", v, "m/s")
# print("Contracted length:", L_prime, "m")

# more reusable python function 
import math 
def length_contraction(l, v):
    c = 299_792_458

    if abs(v) >= c:
        raise ValueError("velocity must be less than the speed of light.")
    
    return L * math.sqrt(1 - (v*2 / c**2))

# Example 
L = 10
v = 0.8 * 299_792_458

print(length_contraction(L, v))
