import pandas as pd
from pathlib import Path
import os

DATA_DIR = Path(__file__).parents[2] / "data/gamma-b"

df = pd.read_csv(DATA_DIR / "to_filter.tsv", delimiter="\t")

#print(df.head())
#print(df.info())
print(df["Assembly Name"].nunique())
print(len(os.listdir(DATA_DIR / "reference_only")))