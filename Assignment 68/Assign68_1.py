image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

feature_map = []

for i in range(len(image) - 2):
    row = []
    for j in range(len(image[0]) - 2):
        total = 0

        for ki in range(3):
            for kj in range(3):
                total += image[i + ki][j + kj] * kernel[ki][kj]

        row.append(total)

    feature_map.append(row)

print("Feature Map:")
for row in feature_map:
    print(row)