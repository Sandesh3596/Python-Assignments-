import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Rename():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df.rename(columns={'Math': 'Mathematics'}, inplace=True)

    print(df)

def main():
    Rename()
if __name__ == "__main__":
    main()