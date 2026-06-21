import pandas as pd

students = {
    "Name": ["Surya", "Rahul", "Aman"],
    "Age": [18, 19, 20]
}

df = pd.DataFrame(students)

print(df)