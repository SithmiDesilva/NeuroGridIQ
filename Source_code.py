# Triangular membership Function
def trimf(x, a, b, c):
    if a == b:
        left = 1.0
        right = (c - x) / (c - b) if c != b else 1.0
    elif b == c:
        left = (x - a) / (b - a) if b != a else 1.0
        right = 1.0
    else:
        left = (x - a) / (b - a) if b != a else 0.0
        right = (c - x) / (c - b) if c != b else 0.0

    return max(min(left, right), 0.0)

# Fuzzy sets for Voltage Deviation (0-100)
def voltage_low(x): return trimf(x, 0, 0, 50)
def voltage_medium(x): return trimf(x, 30, 50, 70)
def voltage_high(x): return trimf(x, 60, 100, 100)

# Fuzzy sets for Frequency Variation (in Hz deviation from 50Hz)
def freq_stable(x): return trimf(x, 0, 0, 0.5)
def freq_unstable(x): return trimf(x, 0.4, 1, 2)

# Fuzzy sets for Load Imbalance (0-100%)
def load_balanced(x): return trimf(x, 0, 0, 20)
def load_unbalanced(x): return trimf(x, 15, 50, 100)

# Fuzzy Rule Evaluation
def fuzzy_rule(voltage, freq, load):
    v_low = voltage_low(voltage)
    v_med = voltage_medium(voltage)
    v_high = voltage_high(voltage)

    f_stable = freq_stable(freq)
    f_unstable = freq_unstable(freq)

    l_bal = load_balanced(load)
    l_unbal = load_unbalanced(load)

    rules = []

    # Rule base with (activation_level, severity_level)
    rules.append((min(v_high, f_unstable, l_unbal), 3))  # High
    rules.append((min(v_med, f_unstable, l_unbal), 2))   # Moderate
    rules.append((min(v_low, f_stable, l_bal), 0))       # No anomaly
    rules.append((min(v_med, f_stable, l_bal), 1))       # Low
    rules.append((min(v_low, f_unstable, l_unbal), 2))   # Moderate
    rules.append((min(v_high, f_stable, l_bal), 2))      # Moderate
    rules.append((min(v_high, f_unstable, l_bal), 2))    # Moderate
    rules.append((min(v_low, f_unstable, l_bal), 1))     # Low
    rules.append((min(v_med, f_unstable, l_bal), 2))     # Moderate
    rules.append((min(v_high, f_stable, l_unbal), 2))    # Moderate

    # Pick rule with highest activation
    activated = max(rules, key=lambda x: x[0])
    return activated[1]

# Defuzzification - Mapping severity to action
def correction_action(severity):
    if severity == 3:
        return "Isolate Faulty Section (High Severity)"
    elif severity == 2:
        return "Perform Load Balancing / Frequency Regulation (Moderate Severity)"
    elif severity == 1:
        return "Adjust Capacitor Banks for Power Factor Correction (Low Severity)"
    else:
        return "No Action Needed (Normal Operation)"
    
    # Simulated Test Cases
test_cases = [
    {"voltage": 90, "freq": 1.5, "load": 80},   # High severity
    {"voltage": 45, "freq": 0.2, "load": 10},   # Normal operation
    {"voltage": 65, "freq": 1.2, "load": 60},   # Moderate severity
    {"voltage": 30, "freq": 0.8, "load": 30},   # Low severity
    {"voltage": 75, "freq": 0.6, "load": 90},   # Moderate severity
    {"voltage": 20, "freq": 2.0, "load": 100},  # High severity
    {"voltage": 50, "freq": 0.1, "load": 5},     # Normal operation
    {"voltage": 10, "freq": 1.0, "load": 50},   # Moderate severity
    {"voltage": 80, "freq": 0.3, "load": 20},   # Low severity
    {"voltage": 55, "freq": 0.4, "load": 15}    # Normal operation
]

# Run and Print Results
print("=== Fuzzy Logic Anomaly Detection & Correction System ===\n")

for i, case in enumerate(test_cases):
    voltage = case["voltage"]
    freq = case["freq"]
    load = case["load"]
    
    severity = fuzzy_rule(voltage, freq, load)
    action = correction_action(severity)
    
    print(f"Test Case {i+1}:")
    print(f"  Voltage Deviation: {voltage}")
    print(f"  Frequency Variation: {freq} Hz")
    print(f"  Load Imbalance: {load}%")
    print(f"  Anomaly Severity Level: {severity}")
    print(f"  Suggested Action: {action}\n")