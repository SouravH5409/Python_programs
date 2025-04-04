import pandas as pd

df = pd.read_csv("employee.csv")

print("First 7 records:\n", df.head(7))

sorted_names = df.sort_values(by="name")["name"]
print("Employees in Alphabetical Order:\n", sorted_names)

highest_salary_employee = df.loc[df["salary"].idxmax()]
print("Employee with Highest Salary:", highest_salary_employee["name"])

male_employees = df[df["gender"].str.lower() == "male"]["name"]
print("Male Employees:\n", male_employees)

teams = df["team"].unique()
print("Teams Employees Belong To:\n", teams)
