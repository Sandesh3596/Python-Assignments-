import numpy as np

data = [-2, -1, 0, 1, 2]

for value in data:
    Ans = np.tanh(value)
    print(value, "->", Ans)