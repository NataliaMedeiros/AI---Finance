from ingestion import load_file
from transformation import transform


file_path = "data/sample.csv"

df = load_file(file_path)

df = transform(df)

print(df)
