import pandas as pd

data = {
    "Name": ["Dev", "Riya", "Aman", "Sam", "Kriti"],
    "Age": [23, 22, 24, 23, 22],
    "Marks": [85, 90, 78, 65, 95]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("✅ students.csv file created")

df = pd.read_csv("students.csv")
print("📂 Loaded Data:\n", df)

print("\n📊 Summary Statistics:")
print(df.describe())

high_scorers = df[df["Marks"] > 80]
print("\n🏆 Students with Marks > 80:\n", high_scorers)

age_22 = df[df["Age"] == 22]
print("\n👩‍🎓 Students aged 22:\n", age_22)
