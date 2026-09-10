import pandas as pd


def load_data(path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)
df = load_data("/Users/heuchennecedric/data-extraction-course/data/graded_Results.csv")
print(df.head())
