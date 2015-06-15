__author__ = 'Su Lei'
import cv2 as cv
import numpy as np

# a = [[1, 0.36], [3, 0.16]]
# 
# def cmp(x, y):
#     if x[1] > y[1]:
#         return 1
#     else:
#         return -1
# 
# # cmp1 = lambda x, y: int(x[1] - y[1])
# a.sort(cmp)
# print a

# f = open('W:\\lsu\\TDI072\\1\\highlight\\test.txt', 'r')
# for i in f:
#     print i

def test():
    a = [1, 2, 3]
    b = 5
    return (a, b)

# m, n = test()
# print m, n
a = np.array(((2, 3, 4), (8, 5, 1)))
print a[1, 2]
print a.take(1, axis=1)
a.put(5, 100)
print a.take(5)
