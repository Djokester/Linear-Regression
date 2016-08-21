import numpy as np
import matplotlib.pyplot as plt
import functools as fn

#Define any Function under the function method.
#By Default I have set it to function(X)=[x^2,y^2,z^2]. Where X = [x,y,z]. 
def function(X): 
    return(np.array([x**2 for x in X]))
    
def partial_derivative_estimate(f, X, i):
    h=10**(-7)    
    Xplus = [xplus + (h if j==i else 0) for j,xplus in enumerate(X)]
    fplus=(f(Xplus))
    fo=f(X)
    return((fplus-fo)/h)

def gradient_estimate():
    
X = [1,2,3]
print(function(X))   
print(partial_derivative_estimate(function, X, 1))