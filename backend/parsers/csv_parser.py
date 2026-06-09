import pandas as pd
import json


def categorize_transaction(description: str) -> str:
    description_upper = description.upper()

    with open("config/category_rules.json") as f:
        CATEGORY_RULES = json.load(f)

    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in description_upper:
                return category

    return "Uncategorized"


def main():
    df = pd.read_csv("sample_data/sample_statement.csv")

    df["category"] = df["description"].apply(categorize_transaction)

    print("\nCategorized Transactions:")
    print(df)

    expenses = df[df["amount"] < 0]

    spending_by_category = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )

    print("\nSpending by Category:")
    print(spending_by_category)

    top_category = spending_by_category.index[0]
    top_amount = spending_by_category.iloc[0]

    print(f"\nTop spending category: {top_category} - ${top_amount:.2f}")


if __name__ == "__main__":
    main()