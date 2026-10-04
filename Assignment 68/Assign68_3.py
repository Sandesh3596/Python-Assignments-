matrix = [
    [6, 4],
    [8, 6]
]

flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Flatten Output: ", flatten_output)