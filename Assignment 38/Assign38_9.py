import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

df.groupby("Final Result")["Assignments Completed"].mean().plot(kind="bar")

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Final Result")
plt.ylabel("Average Assignments Completed")
plt.show()