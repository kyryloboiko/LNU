def sum_of_squares(N):
    result = 0
    for item in range(1, N + 1):
        result += item**2
    return result

print(sum_of_squares(0))
print(sum_of_squares(3))

