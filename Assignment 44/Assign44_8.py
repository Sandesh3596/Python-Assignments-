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

    X = ['English','Math','Science']
    Y = df[df['Name'] == 'Amit'][X].values[0]

    plt.plot(X,Y,marker = "o")
    
    plt.xlabel("# Subjects")
    plt.ylabel("# Marks")
    plt.title("Line Chart for Amit's Performance")
    plt.grid()
    plt.show()

def main():
    DataFrame()

if __name__ =="__main__":
    main()