m = 5
c = -1
x = [0, 1, 2, 3, 4, 5, 6]

y = [i * m + c for i in x]
print(y)

import numpy as np

X = np.array(x)
Y = m * X + c
import matplotlib.pyplot as plt

plt.scatter(X, Y)
