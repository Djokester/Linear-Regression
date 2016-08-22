# Linear-Regression
To implement Gradient Descent, Batch Gradient Descent and Linear Regression. 
If you are unable understand the utility of any function or module please refer to this README for explainations

Important Modules:
1. Numpy
2. Scipy
3. Pandas
4. matplotlib
5. functools
6. 

functools.partial() blocks certain parts of a function and thereby modifies its functionalities
``` python
>>> import functools as fn
>>> def sq(a, b, c):
...   return(a*b*b*c)
>>> sql = fn.partial(sq, 4, c=5)
>>> sql(3)
180
```

The enumerate() function and it's uses has been illustrated below
For a one dimensional array
```python
>>> a = [10, 15, 70, 12, 13 ,14]
>>> for i,val in enumerate(a):
...     print(i, val)
... 
0 10
1 15
2 70
3 12
4 13
5 14
```
For a two dimensional array
```python
>>> b = [[10, 15, 70], [12, 13 ,14], [17,19,21]]
>>> for i,val in enumerate(b):
...     print(i, val)
... 
0 [10, 15, 70]
1 [12, 13, 14]
2 [17, 19, 21]
```
You can further use enumerate() on the variable val at each iteration to get the individual values.
