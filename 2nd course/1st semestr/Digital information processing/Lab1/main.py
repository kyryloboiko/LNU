xk = list(map(int,input("Введiть xk через комy:").split(',')))
yk = list(map(int,input("Bведiть уk через кому:").split(',')))


def discrete_convolution(x, y): 
    I = len(x)
    J = len(y)
    x_reverse = x[::-1]
    result = [0] * (I+J-1)
    for i in range(I):
        for j in range(J):
            result[i + j] += x_reverse[i] * y[j]
    return result[::-1]

print(discrete_convolution(xk,yk))
