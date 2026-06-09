import pandas as pd
from backend.services.categorizer import categorize_transaction

def main():
    df = pd.read_csv("sample_data/sample_data.csv")

    df["category"] = df["description"].apply(categorize_transaction)

    # print("\nCategorized Transactions:")
    # print(df)

    expenses = df[df["amount"] < 0]

    total_expenses = expenses["amount"].abs().sum()

    spending_by_category = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )

    top_category = spending_by_category.index[0]
    top_amount = spending_by_category.iloc[0]

    print("\nStatement Summary")
    print("\nIncome: $2,200")

    print("\nExpenses:")
    print(f"${total_expenses:.2f}")

    print("\nTop Spending Category:") 
    print(f"{top_category}: ${top_amount:.2f}")

    print("\nCategory Breakdown:")
    for category, amount in spending_by_category.items():
        print(f"{category}: ${amount:.2f}")

if __name__ == "__main__":
    main()