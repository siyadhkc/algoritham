import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# ============================================
# SMALL ANGLE PERIOD
# ============================================

def small_angle_period(length, gravity=9.81):
    """
    T = 2π√(L/g)
    """
    return 2 * np.pi * np.sqrt(length / gravity)


# ============================================
# PENDULUM ODE
# ============================================

def pendulum_ode(t, y, length, gravity):
    """
    y[0] = theta
    y[1] = omega
    """

    theta = y[0]
    omega = y[1]

    dtheta_dt = omega
    domega_dt = -(gravity / length) * np.sin(theta)

    return [dtheta_dt, domega_dt]


# ============================================
# LARGE ANGLE NUMERICAL PERIOD
# ============================================

def large_angle_period(
    length,
    theta0_deg,
    gravity=9.81,
    simulation_time=20
):
    """
    Estimate period numerically.
    """

    theta0 = np.radians(theta0_deg)

    # Initial conditions
    y0 = [theta0, 0]

    # Time points
    t_eval = np.linspace(0, simulation_time, 5000)

    # Solve ODE
    solution = solve_ivp(
        pendulum_ode,
        [0, simulation_time],
        y0,
        args=(length, gravity),
        t_eval=t_eval
    )

    theta = solution.y[0]
    time = solution.t

    # Find zero crossings
    crossings = []

    for i in range(1, len(theta)):
        if theta[i - 1] > 0 and theta[i] <= 0:
            crossings.append(time[i])

    if len(crossings) < 2:
        return None

    # Period = 2 * time between crossings
    estimated_period = 2 * (crossings[1] - crossings[0])

    return estimated_period


# ============================================
# COMPARISON
# ============================================

length = 1.0

small_T = small_angle_period(length)

large_T_10 = large_angle_period(length, 10)
large_T_45 = large_angle_period(length, 45)
large_T_90 = large_angle_period(length, 90)

print("================================")
print("SMALL ANGLE APPROXIMATION")
print("================================")
print(f"Small-angle period = {small_T:.5f} s")

print("\n================================")
print("NUMERICAL LARGE-ANGLE PERIODS")
print("================================")
print(f"10°  period = {large_T_10:.5f} s")
print(f"45°  period = {large_T_45:.5f} s")
print(f"90°  period = {large_T_90:.5f} s")


# ============================================
# OPTIONAL PLOT
# ============================================

theta0 = np.radians(90)

solution = solve_ivp(
    pendulum_ode,
    [0, 10],
    [theta0, 0],
    args=(1.0, 9.81),
    t_eval=np.linspace(0, 10, 2000)
)

plt.figure(figsize=(10, 5))
plt.plot(solution.t, np.degrees(solution.y[0]))
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.title("Simple Pendulum Motion")
plt.grid(True)
plt.show()