feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

relu_output = []

for row in feature_map:
    new_row = []

    for value in row:
        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)

print("ReLU Output:")
for row in relu_output:
    print(row)

pool_size = 2
stride = 2

pooled_output = []

for i in range(0, len(relu_output) - pool_size + 1, stride):
    row = []

    for j in range(0, len(relu_output[0]) - pool_size + 1, stride):
        maximum = relu_output[i][j]

        for pi in range(pool_size):
            for pj in range(pool_size):
                value = relu_output[i + pi][j + pj]

                if value > maximum:
                    maximum = value

        row.append(maximum)

    pooled_output.append(row)

print("Max Pooling Output: ")
for row in pooled_output:
    print(row)