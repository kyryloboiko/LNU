import math

def f(x):
    return math.acos(x) - (1 - 0.3 * x**3)**(1/2)

def calc(a, b, N):
    h = (b - a) / (N - 1)

    print("\nResult:")
    for i in range(N):
        x = a + i * h
        y = f(x)
        print(f"x = {x:.4f}, f(x) = {y:.6f}")

a = float(input("a: "))
b = float(input("b: "))
N = int(input("N: "))

while N < 2:
    N = int(input("\nN cannot be less then 2, input correct quantity of iterations: "))
else:
    calc(a, b, N)
