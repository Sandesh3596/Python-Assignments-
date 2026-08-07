import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Average Study Hours by Final Result:")
print(df.groupby("Final Result")["Study Hours"].mean())

print("\nAverage Attendance by Final Result:")
print(df.groupby("Final Result")["Attendance"].mean())
