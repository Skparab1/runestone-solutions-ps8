import math

def approxE(precision):
    calculatede = 0
    i = 0
 
    while abs(math.e-calculatede) > precision:
        calculatede += (1/math.factorial(i))
        i += 1
   
    print('The value of e with precision',precision,'was calculated using',i,'iterations.')
    
    return(calculatede)

print(approxE(0.03))
