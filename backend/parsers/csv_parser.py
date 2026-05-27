import pandas as pd

df = pd.read_csv('sample_data\sample_data.csv')

print(df)

expenses = df[df["amount"] < 0]

total_spent = expenses["amount"].sum()

print(f"total amount spent: {total_spent}:.2f")