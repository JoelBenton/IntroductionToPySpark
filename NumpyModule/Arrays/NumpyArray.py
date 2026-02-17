import numpy as np

python_list = [3,2,5,8,4,9,7,6,1]
array = np.array(python_list)
print(array)
print(type(array))


python_list_of_lists = [
    [3,2,5],
    [9,7,1],
    [4,3,6]
]
array = np.array(python_list_of_lists)
print(array)

print(array.shape)
print(array)


from matplotlib import pyplot as plt
plt.scatter(np.arange(0,7), np.arange(-3, 4))
plt.show()