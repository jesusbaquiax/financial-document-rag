from backend.parsers.csv_parser import parse_csv
from backend.services.summary_service import generate_statement_summary


def main():
    df = parse_csv("sample_data/sample_data.csv")

    summary = generate_statement_summary(df)

    print("\nStatement Summary")
    print(f"\nIncome: ${summary['income']:.2f}")
    print(f"\nExpenses: ${summary['expenses']:.2f}")

    print("\nTop Spending Category:")
    print(f"{summary['top_category']}: ${summary['top_amount']:.2f}")

    print("\nCategory Breakdown:")
    for category, amount in summary["category_breakdown"].items():
        print(f"{category}: ${amount:.2f}")


if __name__ == "__main__":
    main()