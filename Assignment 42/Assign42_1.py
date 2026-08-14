import math

def MarvellousEucDistance(P1, P2):
    return math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)


def MarvellousKNNClassifier(k=3):
    data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'},
        {'point': 'E', 'X': 4, 'Y': 3, 'label': 'Blue'}
    ]

    new_point = {'X':2, 'Y':2}

    for d in data:
        d['Distance'] = MarvellousEucDistance(d, new_point)

    sorted_data = sorted(data, key=lambda item: item['Distance'])
    nearest = sorted_data[:k]

    votes = {}

    for d in nearest:
        label = d['label']
        votes[label] = votes.get(label, 0) + 1

    prediction = max(votes, key=votes.get)

    print("Predicted label:", prediction)


def main():
    MarvellousKNNClassifier(3)


if __name__ == "__main__":
    main()