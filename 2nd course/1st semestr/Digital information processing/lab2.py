xk = list(map(int,input("Введiть xk через комy:").split(',')))
yk = list(map(int,input("Bведiть уk через кому:").split(',')))
scaling = int(input("Введіть множник скаляції:"))


def discrete_convolution(ArrayX = list, ArrayY = list): 
    ArrayXLenght = len(ArrayX)
    ArrayYLenght = len(ArrayY)
    ArrayX_Reverse = ArrayX[::-1]
    Result = [0] * (ArrayXLenght+ArrayYLenght-1)
    for i in range(ArrayXLenght):
        for j in range(ArrayYLenght):
            Result[i + j] += ArrayX_Reverse[i] * ArrayY[j]
    return Result[::-1]

def scale(Array = list, Scaling = int):
    for i in range(len(Array)):
        Array[i] *= Scaling
    return Array
    
    
OutputArray = discrete_convolution(xk, yk)    
print(OutputArray)
print(scale(OutputArray, scaling))
