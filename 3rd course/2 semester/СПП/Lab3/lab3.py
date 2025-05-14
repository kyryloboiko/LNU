from functools import reduce, lru_cache
from timeit import timeit

@lru_cache(maxsize=None)
def fib_rec(n):
    if n <= 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

@lru_cache(maxsize=None)
def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)

def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fact_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fact_reduce(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

def fib_reduce(n):
    if n == 0:
        return 0
    seq = reduce(lambda acc, _: acc + [acc[-2] + acc[-1]], range(n - 2), [0, 1])
    return sum(seq) + 1

def benchmark(n, funcs):
    print(f"n = {n}")
    for name, func in funcs:
        try:
            time = timeit(lambda: func(n), number=1)
            print(f"func = {name}")
            print(f"Execution time {time}")
        except RecursionError:
            print(f"func = {name}")
            print("Execution time = ❌ RecursionError")

if __name__ == '__main__':
    funcs_rec = [("fib_rec", fib_rec), ("fact_rec", fact_rec)]
    funcs = [
        ("fib_loop", fib_loop),
        ("fact_loop", fact_loop),
        ("fact_reduce", fact_reduce),
        ("fib_reduce", fib_reduce),
    ]

    import sys
    sys.setrecursionlimit(1000000)
    sys.set_int_max_str_digits(430000)

    benchmark(10, funcs_rec)
    benchmark(3330, funcs_rec)
    benchmark(10, funcs)
    benchmark(10000, funcs)
