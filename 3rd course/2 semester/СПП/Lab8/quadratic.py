def quadratic(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return "Is Complex"
    elif d == 0:
        x = (-b + d**0.5) / (2 * a)
        return f"{x}"
    else:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return f"{x1}\n{x2}"

print(quadratic(1, -3, 2))
