__author__ = 'Su Lei'

a = [[1, 0.36], [3, 0.16]]

def cmp(x, y):
    if x[1] > y[1]:
        return 1
    else:
        return -1

# cmp1 = lambda x, y: int(x[1] - y[1])
a.sort(cmp)
print a
