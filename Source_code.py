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




