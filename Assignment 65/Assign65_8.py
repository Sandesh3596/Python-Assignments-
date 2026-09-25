import tensorflow as tf

# Input data
x = tf.constant([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

# Weights and bias
weights = tf.Variable([
    [0.1],
    [0.2],
    [0.3]
])

bias = tf.Variable([0.1])

# Linear calculation
z = tf.matmul(x, weights) + bias

# Sigmoid output layer
output = tf.nn.sigmoid(z)

print("Sigmoid Output:")
print(output)