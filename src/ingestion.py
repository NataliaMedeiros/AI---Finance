from pathlib import Path
# Use Path is not mandatory to read the file, but I choose to use it because I can have
# Useful information about the file_path, such as the extension.

import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_excel(file_path):
	return pd.read_excel(file_path)

def load_file(file_path):
	file_path = Path(file_path) # Transform the string path to an object Path
	extension = file_path.suffix.lower()
	if extension == ".csv":
		return load_csv(file_path)
	if extension in [".xlsx", ".xls"]:
		return load_excel(file_path)
	raise ValueError(f"Unsupported file format: {extension}")
