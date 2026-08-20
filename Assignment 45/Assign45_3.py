import pandas as pd

def Average():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df['Gender'] = ['Male', 'Male', 'Female']

    print(df)

    average = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print(average)


def main():
    Average()
if __name__ == "__main__":
    main()