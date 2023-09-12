xk = list(map(int,input("Введiть xk через комy:").split(',')))
yk = list(map(int,input("Bведiть уk через кому:").split(',')))


def discrete_convolution(x, y): 
    I = len(x)
    J = len(y)
    result = [0] * (I+J-1)
    print(result)
    for i in range(I):
        for j in range(J):
            result[i + j] += x[i] * y[j]
    return result

print(discrete_convolution(xk,yk))