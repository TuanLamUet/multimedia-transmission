import math

def prob(n, p):
	return ((1-p)**(n-1))*p

def infoMeasure(n, p):
    return float(-math.log2(prob(n,p)))

def sumProb(N, p):              
    sum = 0                    
    for i in range(1, N + 1):  
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):                        
    entropy = 0                                
    for i in range(1, N + 1):                   
        entropy+=prob(i, p)*infoMeasure(i, p)   
    return entropy
