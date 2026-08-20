import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def BoxPlot():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    plt.boxplot(df['English'])
    plt.ylabel("English Marks")
    plt.title("English Marks Boxplot")
    plt.show()

def main():
    BoxPlot()
if __name__ == "__main__":
    main()