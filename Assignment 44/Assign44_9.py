import pandas as pd
import numpy as np

def DataFrame():
    data2 = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[np.nan, 90, 88],
        'Science':[91, np.nan, 85]
    }

    df = pd.DataFrame(data2)

    print("DataFrame Before Filling Missing Values:")
    print(df)

    df['Math'] = df['Math'].fillna(df['Math'].mean())
    df['Science'] = df['Science'].fillna(df['Science'].mean())

    print("DataFrame After Filling Missing Values with mean:")
    print(df)

def main():
    DataFrame()

if __name__ == "__main__":
    main()