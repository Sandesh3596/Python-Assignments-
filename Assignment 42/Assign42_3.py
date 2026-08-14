import math

def MarvellousEucDistance(P1, P2):
    return math.sqrt((P1['Study Hours'] - P2['Study Hours']) ** 2 +
                     (P1['Attendance'] - P2['Attendance']) ** 2)


def MarvellousKNNClassifier(k=3):
    data = [
        {'Study Hours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'Study Hours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'Study Hours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'Study Hours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    new_point = {
        'Study Hours': 4,
        'Attendance': 70
    }

    for d in data:
        d['Distance'] = MarvellousEucDistance(d, new_point)

    sorted_data = sorted(data, key=lambda item: item['Distance'])
    nearest = sorted_data[:k]

    votes = {}

    for d in nearest:
        result = d['Result']
        votes[result] = votes.get(result, 0) + 1

    prediction = max(votes, key=votes.get)

    print("Predicted Result:", prediction)


def main():
    MarvellousKNNClassifier(3)


if __name__ == "__main__":
    main()