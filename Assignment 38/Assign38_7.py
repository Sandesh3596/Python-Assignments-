import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

colors = {0: "red", 1: "green"}

for result in df["Final Result"].unique():
    temp = df[df["Final Result"] == result]
    plt.scatter(temp["Study Hours"], temp["Previous Score"],
                color=colors[result],
                label=f"Result {result}")

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend()
plt.grid()
plt.show()