import numpy
import numpy as np

a = np.arange(12)
print(a)
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[:, 0])
floats=numpy.loadtxt('floats-10M-lines.txt')
print(floats[-3:])