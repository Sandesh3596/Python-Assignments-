import pandas as pd

def Normalized():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    df = pd.DataFrame(data)
    df['Gender'] = ['Male', 'Male', 'Female']

    df = pd.get_dummies(df, columns=['Gender'], dtype=int)

    print(df)

def main():
    Normalized()
if __name__ == "__main__":
    main()