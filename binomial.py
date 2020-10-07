import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def prob(n, p, N):
    return nCr(N, n)*(((1-p)**(N-n))*(p**n))
    
    
def infoMeasure(n, p, N):
    return float(-math.log2(prob(n,p,N)))
    
    
def sumProb(N, p):              
    sum = 0                     
    for i in range(0, N + 1):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):                           
    entropy = 0                                    
    for i in range(0, N + 1):                       
        entropy+=prob(i, p, N)*infoMeasure(i, p, N) 
    return entropy
