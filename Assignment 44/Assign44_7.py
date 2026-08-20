import pandas as pd
import matplotlib.pyplot as plt

def DataFrame():
    Data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(Data)
    df['Total'] = df['Math'] + df['Science'] + df['English']

    df = df.sort_values("Total",ascending= False)
    #create bar plot : Student Name vs Total
    X = df['Name']
    Y = df['Total']
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.bar(X,Y)
    plt.title("Students Performance")
    plt.show()

def main():
    DataFrame()

if __name__ =="__main__":
    main()