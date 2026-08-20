import pandas as pd

STANDARD_COLUMNS = [
    "date",
    "description",
    "transaction_type",
    "amount",
]

COLUMN_ALIASES = {
    "date": [
        "date",
        "booking date",
        "transaction date",
    ],

    "description": [
        "name",
        "description",
        "name / description",
        "counterparty",
    ],

    "transaction_type": [
        "debit/credit",
        "credit/debit",
    ],

	"debit": [
		"debit",
	],

	"credit": [
		"credit",
	],

    "amount": [
        "amount",
        "amount (eur)",
        "transaction amount",
    ],
}

def normalize_column_names(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    return df

def find_column(df, aliases):
	normalized_columns = {
		column.strip().lower().replace(" ", ""): column
		for column in df.columns
	}
	for alias in aliases:
		normalized_alias = alias.strip().lower().replace(" ", "")
		if normalized_alias in normalized_columns:
			return normalized_columns[normalized_alias]

	return None

def validate_debit_credit(df, debit_column, credit_column):
    debit_filled = df[debit_column].notna() #notna is a panda function that checks if the falue is not empty and returns true or false
    credit_filled = df[credit_column].notna()

    if (debit_filled & credit_filled).any():
        raise ValueError(
            "A transaction cannot have both debit and credit."
        )

    if (~debit_filled & ~credit_filled).any():
        raise ValueError(
            "A transaction must have either debit or credit."
        )


def transform(df):
	df = df.copy()
	df.columns = (df.columns .str.strip() .str.lower())

	print(list(df.columns))

	date_column = find_column(df, COLUMN_ALIASES["date"])
	description_column = find_column(df, COLUMN_ALIASES["description"])
	transaction_type_column = find_column(df, COLUMN_ALIASES["transaction_type"])
	amount_column = find_column(df, COLUMN_ALIASES["amount"])
	debit_column = find_column(df,COLUMN_ALIASES["debit"])
	credit_column = find_column(df,COLUMN_ALIASES["credit"])

	print("date_column:", date_column)
	print("description_column:", description_column)
	print("transaction_type_column:", transaction_type_column)
	print("amount_column:", amount_column)
	print("debit_column:", debit_column)
	print("credit_column:", credit_column)

	# return df

	transformed_df = pd.DataFrame()

	transformed_df["date"] = df[date_column]
	transformed_df["description"] = df[description_column]
	if (transaction_type_column and amount_column):
		transformed_df["transaction_type"] = df[transaction_type_column]
		transformed_df["amount"] = df[amount_column]
	elif (debit_column and credit_column):
		validate_debit_credit(df, debit_column, credit_column)
		debit_filled = df[debit_column].notna()
		credit_filled = df[credit_column].notna()
		transformed_df["transaction_type"] = "debit"
		transformed_df.loc[
			credit_filled,
			"transaction_type"
		] = "credit"
		transformed_df["amount"] = (
		df[debit_column]
		.fillna(df[credit_column])
	)
	else:

		raise ValueError("Could not identify a valid transaction format.")
	return transformed_df
