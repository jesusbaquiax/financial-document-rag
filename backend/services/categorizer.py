import json

def categorize_transaction(description: str) -> str:
    description_upper = description.upper()

    with open('backend/config/category_rules.json') as f:
        CATEGORY_RULES = json.load(f)

    for category, keywords in CATEGORY_RULES.items():
        for keyword in keywords:
            if keyword in description_upper:
                return category

    return "Uncategorized"