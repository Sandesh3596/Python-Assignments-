import numpy as np

data = [4, 6, 8, 10, 12]

mean = np.mean(data)
deviation = [x - mean for x in data]
squared_deviation = [x ** 2 for x in deviation]
variance = np.var(data)

print("Mean of data: ", mean)
print("Deviation of data: ", deviation)
print("Squared Deviation of data: ", squared_deviation)
print("Variance of data: ", variance)