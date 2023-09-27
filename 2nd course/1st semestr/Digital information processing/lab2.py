xk = list(map(int,input("Введiть xk через комy:").split(',')))
yk = list(map(int,input("Bведiть уk через кому:").split(',')))


def discrete_convolution(ArrayX = list, ArrayY = list, ExpandX = 1, ExpandY = 1): 
    ArrayXLenght = len(ArrayX)
    ArrayYLenght = len(ArrayY)
    
    ArrayX_Reverse = ArrayX[::-1]
    Result = [0] * (ArrayXLenght+ArrayYLenght-1)
    
    for i in range(ArrayXLenght):
        ArrayX *= ExpandX
        
    for i in range(ArrayYLenght):
        ArrayY *= ExpandY
        
    for i in range(ArrayXLenght):
        for j in range(ArrayYLenght):
            Result[i + j] += ArrayX_Reverse[i] * ArrayY[j]
    return Result[::-1]

def scale(Array = list, Scaling = float):
    Result = [0] * len(Array)
    for i in range(len(Array)):
        Result[i] = Array[i] * Scaling
    return Result
    
def time_reverse(Array = list):
    Result = [0] * len(Array)
    for i in range(len(Array)):
        Result[i] = Array[i]
    return Result[::-1]    

def shift(Array = list):
    Result = [0] * len(Array)
    for i in range(len(Array)):
        Result[i] = Array[i]
        Result[i] *= -1
    return Result

def multiply(ArrayX = list, ArrayY = list):
    ArrayXLenght = len(ArrayX)
    ArrayYLenght = len(ArrayY)
    Result = []
    if ArrayXLenght >= ArrayYLenght:
        difference = ArrayXLenght - ArrayYLenght
        for i in range(difference):
            ArrayY.append(0)
        for i in range(ArrayXLenght):
            Result.append(0)
            Result[i] = ArrayX[i] * ArrayY[i]
        return Result
    else:
        difference = ArrayYLenght - ArrayXLenght
        for i in range(difference):
            ArrayX.append(0)   
        for i in range(ArrayYLenght):
            Result.append(0)
            Result[i] = ArrayX[i] * ArrayY[i]
        return Result

def addition(ArrayX = list, ArrayY = list):
    ArrayXLenght = len(ArrayX)
    ArrayYLenght = len(ArrayY)
    Result = []    
    difference = ArrayXLenght - ArrayYLenght
    if difference >= 0:
        for i in range(difference):
            ArrayY.append(0)
        for i in range(ArrayXLenght):
            Result.append(0)
            Result[i] = ArrayX[i] + ArrayY[i]
        return Result
    if difference < 0:
        for i in range(difference*-1):
            ArrayX.append(0)
        for i in range(ArrayXLenght):
            Result.append(0)
            Result[i] = ArrayX[i] + ArrayY[i]
        return Result
        
    
    
print(scale(xk,2))
print(shift(xk))
print(time_reverse(xk))
print(discrete_convolution(xk,xk,2))
print(multiply(xk,yk))
print(addition(xk,yk))
