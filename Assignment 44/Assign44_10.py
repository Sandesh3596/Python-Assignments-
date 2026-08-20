import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def DataFrame():
    Data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(Data)

    df = df.drop('English', axis=1)
    print(df)

def main():
    DataFrame()

if __name__ =="__main__":
    main()