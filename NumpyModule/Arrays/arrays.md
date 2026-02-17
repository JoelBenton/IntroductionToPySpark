# Numpy Arrays
The main object in numpy, it's a grid -like structure that holds data. An array can have any number of dimensions and each dimension can be any length
![ArrayPicExample.png](Pictures/ArrayPicExample.png)


# How to create a Numpy Array
First Import The Numpy module using
```python
import numpy as np
```
## Creating a 1D array from lists
To Create a 1D numpy array from a list, you simply need to pass it a list of data and it will make a numpy array containing that data
```python
python_list = [3,2,5,8,4,9,7,6,1]
array = np.array(python_list)
print(array)
# Output: [3 2 5 8 4 9 7 6 1]
print(type(array))
# Output: <class 'numpy.ndarray'>
```

## Creating a 2D array from lists
Same as a 1D array, however instead you pass it a list of lists instead.
```python
python_list_of_lists = [
    [3,2,5],
    [9,7,1],
    [4,3,6]
]
array = np.array(python_list_of_lists)
print(array)
# Output:
# [[3 2 5]
# [9 7 1]
# [4 3 6]]
```
## Creating arrays from scratch
There are many NumPy functions used to create arrays fom scratch, including:
- `np.zeros((x,y))`
  - Creates an array of zero's depending on the parameters given in an Integer Tuple (X,Y). X being Width and Y being Height.
  - Good for creating an array and filling with data later on.
- `np.random.random((x,y))`
  - Creates an array of random numbers between 1 and 0 depending on the parameters given in a Integer Tuple (X,Y). X being Width and Y being Height.
  -  It contains .random twice as `np.random` is the random module in numpy and the second `.random` is the function name within the module.
- `np.arange(x,y,z)`
  - Creates an evenly-spaced array of numbers based on a given start (x) and stop (y) values.
  - By default, it will create an array of sequential integers. The start value is included in the output array, but the stop value is not.
  - If a third argument (z) is passed, it is interpreted as a step value. Now the desired distance between elements is that Z Value.
  - `np.arange()` is useful for plotting.
  - ```python
    from matplotlib import pyplot as plt
    plt.scatter(np.arange(0,7),
                np.arange(-3, 4))
    ```
    ![NumpyArrangePlotExample.png](Pictures/NumpyArrangePlotExample.png)

# Why use arrays instead of lists
## Python Lists
- Can contain many different data types.
```python
python_list = ['beep', False, 56, .945, [3,2,5]]
```
## Numpy Lists
- Can contain only a single data type.
```python
numpy_boolean_array = [[True, False], [True, True], [False, True]]
numpy_float_array = [1.9, 5.4, 8.8, 3.6, 3.2]
```
## why?
With Numpy arrays allowing only a single data type, it makes it very efficient.
As there is no need to check the data type of each element as in an array, they all must be the same.
Having only a single data type also means that a NumPy array takes up less space in the memory than the same information would if stored as a python list.

