import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Histogram():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    import matplotlib.pyplot as plt

    plt.hist(df['Math'])
    plt.xlabel("Math Marks")
    plt.ylabel("Number of Students")
    plt.title("Math Marks Histogram")
    plt.show()

def main():
    Histogram()
if __name__ == "__main__":
    main()