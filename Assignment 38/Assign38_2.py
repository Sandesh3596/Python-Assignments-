import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

Total_Students = len(df)

Students_Passed = (df["Final Result"] == 1).sum()

Studets_Failed = (df["Final Result"] == 0).sum()

print("Total Students :", Total_Students)
print("Passed Students :", Students_Passed)
print("Total Failed Students :", Studets_Failed)