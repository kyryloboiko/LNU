import math

def f(x):
    return x - 2 + math.sin(1/x)

def calc_by_steps_quantity(a, b, N):
    h = (b - a) / (N - 1)

    print("\nResult:")
    for i in range(N):
        x = a + i * h
        y = f(x)
        print(f"x = {x:.4f}, f(x) = {y:.6f}")

def calc_by_step_size(a, b, step_size):
    print("\nResult:")
    x = a
    while x <= b + step_size/2:
        y = f(x)
        print(f"x = {x:.4f}, f(x) = {y:.6f}")
        x += step_size

a = float(input("a: "))
b = float(input("b: "))

choice = input("Choose input method:\n1 - Number of steps\n2 - Step size\n")

if choice == '1':
    N = int(input("N: "))
    while N < 2:
        N = int(input("\nN cannot be less than 2, input correct quantity of iterations: "))
    else:
        calc_by_steps_quantity(a, b, N)
elif choice == '2':
    step_size = float(input("Enter step size: "))
    calc_by_step_size(a, b, step_size)
else:
    print("Invalid choice.")
