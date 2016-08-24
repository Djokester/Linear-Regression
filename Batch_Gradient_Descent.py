import numpy as np
import matplotlib.pyplot as plt
import functools as fn
import random 
import pandas as pd

#define the Cost Function
def cost_function(X, y, theta):
    J = (np.sum((np.dot(theta,X) - y)**2))/(2*len(y)) #J represents the Cost.
    return J

#define the gradient descent
def gradient_descent(X, y, iterations, theta, alpha):
    J_log = []
    while iterations>0:
        iterations-=1
        cost = cost_function(X, y, theta)
        J_log.append(cost)
        theta=theta - alpha/len(y)*(np.dot((np.dot(theta,X)-y),X.transpose()))
    return (theta,J_log)                
            
#import the dataset with Pandas.
data = pd.read_csv('ex1data1.txt', names = ['population', 'profit'])
print(data.head())
X = np.array(data.population)
y = np.array(data.profit)

#plot the dataset as a scatter plot
plt.plot(data.population, data.profit)
plt.show()
iterations= 40000

X = np.array([np.ones(len(y)), X])
theta = np.zeros(2).transpose()
alpha=0.00001
print(gradient_descent(X,y,iterations, theta, alpha)) 
