def generate_statement_summary(df):
    income = df[df["amount"] > 0]["amount"].sum()

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

    return {
        "income": income,
        "expenses": total_expenses,
        "top_category": top_category,
        "top_amount": top_amount,
        "category_breakdown": spending_by_category.to_dict(),
    }