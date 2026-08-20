import pandas as pd

def DataFrame():
    Data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English': [75,85,82]
    }

    df = pd.DataFrame(Data)
    df['Total'] = df['Math'] + df['Science'] + df['English']

    print(df)

    if (df['Science']> 85).any():
         print(df[df['Science'] > 85]['Name'])
    else:
        print("No student scored above 85")


def main():
    DataFrame()

if __name__ =="__main__":
    main()