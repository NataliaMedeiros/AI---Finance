from ingestion import load_file


file_path = "data/sample.csv"

df = load_file(file_path)

print(df)
