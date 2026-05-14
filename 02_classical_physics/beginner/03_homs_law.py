# ============================================
# OHM'S LAW + CIRCUIT SOLVER
# ============================================

from typing import List


# ============================================
# BASIC OHM'S LAW FUNCTIONS
# ============================================

def calculate_voltage(current: float, resistance: float) -> float:
    """
    V = I * R
    """
    return current * resistance


def calculate_current(voltage: float, resistance: float) -> float:
    """
    I = V / R
    """
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")

    return voltage / resistance


def calculate_resistance(voltage: float, current: float) -> float:
    """
    R = V / I
    """
    if current == 0:
        raise ValueError("Current cannot be zero.")

    return voltage / current


# ============================================
# SERIES CIRCUIT
# ============================================

def series_resistance(resistors: List[float]) -> float:
    """
    Total resistance in series:
    R_total = R1 + R2 + R3 + ...
    """
    return sum(resistors)


# ============================================
# PARALLEL CIRCUIT
# ============================================

def parallel_resistance(resistors: List[float]) -> float:
    """
    Total resistance in parallel:
    1/R = 1/R1 + 1/R2 + ...
    """

    if len(resistors) == 0:
        raise ValueError("Resistor list cannot be empty.")

    reciprocal_sum = 0

    for r in resistors:
        if r == 0:
            raise ValueError("Resistance cannot be zero.")

        reciprocal_sum += 1 / r

    return 1 / reciprocal_sum


# ============================================
# POWER FUNCTIONS
# ============================================

def power_vi(voltage: float, current: float) -> float:
    """
    P = V * I
    """
    return voltage * current


def power_i2r(current: float, resistance: float) -> float:
    """
    P = I^2 * R
    """
    return current ** 2 * resistance


def power_v2r(voltage: float, resistance: float) -> float:
    """
    P = V^2 / R
    """
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")

    return (voltage ** 2) / resistance


# ============================================
# UNIVERSAL OHM'S LAW SOLVER
# ============================================

def solve_ohms_law(
    voltage=None,
    current=None,
    resistance=None
):
    """
    Provide ANY TWO values and compute the third.
    """

    values_provided = sum(
        x is not None for x in [voltage, current, resistance]
    )

    if values_provided != 2:
        raise ValueError(
            "You must provide exactly TWO values."
        )

    # Find Voltage
    if voltage is None:
        voltage = calculate_voltage(current, resistance)

    # Find Current
    elif current is None:
        current = calculate_current(voltage, resistance)

    # Find Resistance
    elif resistance is None:
        resistance = calculate_resistance(voltage, current)

    return {
        "Voltage (V)": voltage,
        "Current (I)": current,
        "Resistance (R)": resistance
    }


# ============================================
# EXAMPLES
# ============================================

print("================================")
print("OHM'S LAW")
print("================================")

result = solve_ohms_law(
    current=2,
    resistance=5
)

print(result)

# Expected:
# Voltage = 10V


print("\n================================")
print("SERIES CIRCUIT")
print("================================")

series = series_resistance([2, 3, 5])

print(f"Series Resistance = {series} Ohms")

# Expected:
# 10 Ohms


print("\n================================")
print("PARALLEL CIRCUIT")
print("================================")

parallel = parallel_resistance([6, 3])

print(f"Parallel Resistance = {parallel:.2f} Ohms")

# Expected:
# 2 Ohms


print("\n================================")
print("POWER")
print("================================")

power = power_vi(12, 3)

print(f"Power = {power} Watts")

# Expected:
# 36 Watts