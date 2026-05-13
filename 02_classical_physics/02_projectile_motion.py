import math

def projectile_motion(u, theta_deg, g=9.81):

    theta = math.radians(theta_deg)

    # Time of flight
    T = (2 * u * math.sin(theta)) / g

    # Maximum height
    H = (u**2 * (math.sin(theta))**2) / (2 * g)

    # Horizontal range
    R = (u**2 * math.sin(2 * theta)) / g

    print(f"Initial Speed = {u} m/s")
    print(f"Launch Angle = {theta_deg}°")

    print(f"\nTime of Flight = {T:.2f} s")
    print(f"Maximum Height = {H:.2f} m")
    print(f"Range = {R:.2f} m")

    print("\nTrajectory Table")
    print("-" * 30)
    print("t(s)\tx(m)\ty(m)")

    steps = 10

    for i in range(steps + 1):

        t = (T / steps) * i

        x = u * math.cos(theta) * t

        y = (
            u * math.sin(theta) * t
            - 0.5 * g * t**2
        )

        print(f"{t:.2f}\t{x:.2f}\t{y:.2f}")


# Example
projectile_motion(20, 45)