from math import log, sqrt, exp

def task13(t, x):
     return exp(t + 0.5)+log(sqrt(exp(2*x) - t** 2))+(log(x** 2))**2 

t = 2
x = 3

print(task13(t, x))