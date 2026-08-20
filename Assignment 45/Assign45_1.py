import pandas as pd

def Scores():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    df = pd.DataFrame(data)
    df['Math_Normalized'] = (df['Math'] - df['Math'].min()) /(df['Math'].max() - df['Math'].min())

    print("The normalizaed Math is: \n", df['Math_Normalized'])

    print(df)

def main():
    Scores()
if __name__ == "__main__":
    main()