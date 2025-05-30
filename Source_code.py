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
