import pandas as pd

#all concepts 


# Employee data
employees = {
    "Name": ["Alex", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [60000, 45000, 72000, 55000, 48000, 65000]
}

df = pd.DataFrame(employees)

print("Employee Data")
print(df)

# Add bonus (10%)
df["Bonus"] = df["Salary"] * 0.10

# Total salary after bonus
df["Total Salary"] = df["Salary"] + df["Bonus"]

print("\nUpdated Employee Data")
print(df)

# Employees earning above 50,000
print("\nEmployees earning above 50,000")
print(df[df["Salary"] > 50000])

# Average salary by department
print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

# Highest paid employee
highest = df.loc[df["Salary"].idxmax()]
print("\nHighest Paid Employee")
print(highest)

# Save to CSV
df.to_csv("employee_report.csv", index=False)

print("\nEmployee report saved successfully!")