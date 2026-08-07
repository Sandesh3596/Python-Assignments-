import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

result = df["Final Result"].value_counts()

print("Distribution of Final Result")
print(result)

Total_Students = len(df)
print("Total Students :", Total_Students)

pass_percentage = (result[1] / Total_Students) * 100
fail_percentage = (result[0] / Total_Students) * 100

print("\nPass Percentage : {:.2f}%".format(pass_percentage))
print("Fail Percentage : {:.2f}%".format(fail_percentage))

if abs(pass_percentage - fail_percentage) <= 10:
    print("\nDataset is Balanced.")
else:
    print("\nDataset is Not Balanced.")