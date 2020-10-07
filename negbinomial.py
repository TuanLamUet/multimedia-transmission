import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def prob(n, p, r):
    return nCr(n-1, r-1)*(p**r)*(1-p)**(n-r)
def infoMeature(n, p, r):
    return float(-math.log2(prob(n, p, r)))

def sumProb(N, p, r):           
    sum = 0                         
    for i in range(r, N + 1):
        sum+=prob(i, p, r)
    return sum
    
def approxEntropy(N, p, r):                             
    entropy = 0                                         
    for i in range(r, N + 1):                          
        entropy += prob(i, p, r)*infoMeature(i, p, r)   
    return entropy
