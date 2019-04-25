# %%
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mat
# import math as math
N = 20000
kukan = 20.0
h = kukan / N
Y = 3.0
X = -1.0
Y_new = 3.0

X_new = -1.0
T = 0  # Tはtimeを表す
x = np.zeros(int(N / 50))
y = np.zeros(int(N / 50))
t = np.zeros(int(N / 50))
sub = np.zeros(int(N / 50))


def integral_1(t, x, y):
    return y


def integral_2(t, x, y):
    return -2 * x - 3 * y


for count in range(N):
    if count % 50 == 0:
        T = count * h
        sub[int(count / 50)] = np.exp((-3 + np.sqrt(5) * T / 2))
        Y_new = Y + h * integral_2(T, X, Y)
        X_new = X + h * integral_1(T, X, Y)
        y[int(count / 50)] = Y_new
        x[int(count / 50)] = X_new
        t[int(count / 50)] = T
        Y = Y_new
        X = X_new
        print(sub[int(count / 50)], T)
mat.plot(t, sub)
# mat.plot(t, y)
mat.show()
