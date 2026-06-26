import pandas as pd

students = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Marks": [88, 95, 79, 91]
}

df = pd.DataFrame(students)

print(df)
print("Average Marks:", df["Marks"].mean())
