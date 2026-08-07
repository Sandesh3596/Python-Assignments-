import pandas as pd
import math

df = pd.read_csv("student_performance_ml.csv")

print("The Average Study Hours :", df["Study Hours"].mean())
print("The Average Attendance :", df["Attendance"].mean())
print("The Maximum Previous Score :", df["Previous Score"].max())
print("The Minimum Sleep Hours :", df["Sleep Hours"].min())