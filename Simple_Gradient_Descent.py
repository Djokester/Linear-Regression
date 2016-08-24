import numpy as np
import matplotlib.pyplot as plt
import functools as fn
import random 

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Define any Function under the function method.
#By Default I have set it to function(X)=[x^2,y^2,z^2]. Where X = [x,y,z]. 
def function(X): 
    return(sum([x**2 for x in X]))
    
def partial_derivative_estimate(f, X, i):
    h=10**(-7)    
    Xplus = [xplus + (h if j==i else 0) for j,xplus in enumerate(X)]
    fplus=(f(Xplus))
    fo=f(X)
    return((fplus-fo)/h)

def gradient_estimate(f, X):
    return([partial_derivative_estimate(f, X, i) for i in range(0,len(X))])
    
def step(X,gradient,h):
    return([y-x*h for y,x in zip(X,gradient)])
    
step_multiplier = 0.00001
v = [random.randint(-10,10) for i in range(3)]
tolerance=0.000001
while True:
    gradient = gradient_estimate(function, v)
    next_v = step(v,gradient,0.001)
    if sum([(x-y)**2 for x,y in zip(v, next_v)]) < tolerance**2:
            break
    v = next_v
  
    
print(v)