import numpy as np
import matplotlib.pyplot as plt
import functools as fn
import random 
import pandas as pd

#define the sigmoid function.
def sigmoid(a):
    return(1/(1+np.exp(-a)))
    
#define the cost function
def cost_function(X, y, theta):
        h = np.dot(theta,X)
        return(-np.dot(y,np.log(h))-np.dot((1-y),np.log(1-h)))

#define gradient descent 
def gradient_descent(X, y, iterations, theta, alpha):
    J_log = []
    while iterations>0:
        iterations-=1
        cost = cost_function(X, y, theta)
        J_log.append(cost)
        theta=theta - alpha/len(y)*(np.dot((sigmoid(np.dot(theta,X))-y),X.transpose()))
    return (theta,J_log)    
    

#import the dataset with Pandas.
data = pd.read_csv('ex2data1.txt', names=['x1','x2','y'])

y = np.array(data.y)
X = np.array([np.ones(len(y)), data.x1 , data.x2])
print(data.head)
print(X)
print(y)

iterations = 1000
theta = np.array([0, 0, 0])
print(gradient_descent(X, y, iterations, theta, 0.01))

# Specified in plot order


