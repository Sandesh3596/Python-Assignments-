import pandas as pd
import matplotlib.pyplot as plt

def Average():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    sagar = df[df['Name'] == 'Sagar']
    marks = sagar[['Math', 'Science', 'English']].iloc[0]

    plt.pie(
        marks,
        labels=marks.index,
        autopct='%1.1f%%'
    )
    
    plt.title("Sagar's Marks")
    plt.show()

def main():
    Average()
if __name__ == "__main__":
    main()