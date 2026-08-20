import pandas as pd

def DataFrame():
    Data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(Data)
    print("The Shape of Dataset is: ",df.shape)
    print("Name of Columns in Dataset: ",df.columns)
    print("Data Type of Dataset: ",df.dtypes)


def main():
    DataFrame()

if __name__ =="__main__":
    main()