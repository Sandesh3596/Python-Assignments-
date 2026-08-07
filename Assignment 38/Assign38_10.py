import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

df.boxplot(column="Sleep Hours", by="Final Result")

plt.title("Sleep Hours vs Final Result")
plt.suptitle(" ")
plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")
plt.show()