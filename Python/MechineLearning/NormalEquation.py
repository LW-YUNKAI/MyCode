import numpy as np

# y = 3 + 2 * x1 + 1 * x2
x_train = np.array([[1, 2], [2, 1], [2, 3], [3, 5], [1, 3], [4, 2], [7, 3], [4, 5], [11, 3], [8, 7]])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])

X = np.mat(np.zeros((len(x_train), 3)))


# 形成新向量
def newArray(l):
    c = len(l) + 1
    newA = np.array(np.zeros(c))
    newA[0] = 1
    i = 1
    while i < c:
        newA[i] = l[i - 1]
        i += 1
    return newA


i = 0

# 化为矩阵
while i < np.shape(X)[0]:
    thisArray = newArray(x_train[i])
    X[i] = thisArray
    # a1[i][1] = x_train[i][0]
    # a1[i][2] = x_train[i][1]
    i += 1

Y = np.mat(y_train).T
XT = X.T

Theta = (XT * X).I * XT * Y
print(Theta)
