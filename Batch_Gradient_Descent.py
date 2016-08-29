import numpy as np
import matplotlib.pyplot as plt
import functools as fn
import random 
import pandas as pd
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


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
iterations= 400


X = np.array([np.ones(len(y)), X])
theta = np.zeros(2).transpose()
alpha=0.0001
print(gradient_descent(X,y,iterations, theta, alpha)) 

theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)

# initialize J_vals to a matrix of 0's
J_vals = np.zeros((len(theta0_vals),len(theta1_vals)))

# Fill out J_Vals 
# Note: There is probably a more efficient way to do this that uses
#	broadcasting instead of the nested for loops
for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        t = np.array([theta0_vals[i],theta1_vals[j]])
        J_vals[i][j] = cost_function(X,y,t)


# Surface plot using J_Vals
fig = plt.figure()
ax = plt.subplot(111,projection='3d')
Axes3D.plot_surface(ax,theta0_vals,theta1_vals,J_vals,cmap=cm.coolwarm)
plt.show()


