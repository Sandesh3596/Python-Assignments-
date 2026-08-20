import pandas as pd
import numpy as np

def Status():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df['Status'] = df['Math'] + df['Science'] + df['English']

    print(df)

    passed = (df['Status'] >= 250).sum()
    print("Pass Students: ", passed)

    df.to_csv("students.csv", index=False)
def main():
    Status()
if __name__ == "__main__":
    main()