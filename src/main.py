import pandas as pd

CATEGORIES = {
    "albert heijn": "Groceries",
    "jumbo": "Groceries",
    "uber eats": "Restaurants",
    "kfc": "Restaurants",
    "ns": "Transport",
    "shell": "Transport",
    "spotify": "Entertainment",
    "netflix": "Entertainment",
    "coolblue": "Shopping",
    "apple": "Shopping",
    "ikea": "Shopping",
}

def categorize(description):
    description = description.lower()

    for merchant, category in CATEGORIES.items():
        if merchant in description:
            return category

    return "Other"

file_path = "data/sample.csv"

transactions = pd.read_csv(file_path)

transactions["category"] = transactions["description"].apply(categorize)

print(transactions)

total = transactions["amount"].sum() * -1

print(f"Total: €{total:.2f}")
