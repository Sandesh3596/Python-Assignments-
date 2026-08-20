def Salaryprediction(experience):
    return 12 * experience + 25

for experience in [2, 5, 7]:
    salary = Salaryprediction(experience)
    print("Experience:", experience, "years")
    print("Predicted Salary:", salary)

