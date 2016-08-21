# Machine-Learning-Algorithms
To implement Gradient Descent, Linear Regression, Normalization, Clustering and other Machime Learning Algorithms. 
If you are unable understand the utility of any function or module please refer to this README for explainations

Important Modules:
1. Numpy
2. Scipy
3. Pandas
4. matplotlib
5. functools
6. 

functools.partial() blocks certain parts of a function and thereby modifies its functionalities
...
 import functools as fn
 def sq(a, b, c):
 return(a*b*b*c)

 sql = fn.partial(sq, 4, c=5)
 sql(3)
180
...
