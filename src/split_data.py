import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "SouthGermanCredit.asc"
df = pd.read_csv(DATA_FILE, sep=r"\s+", header=0)
print(df.shape)
print(df.isnull().sum().sum())

train_df,temp_df = train_test_split(df,test_size = 0.3,stratify=df["kredit"], random_state=42)
print(train_df.shape)
print(temp_df.shape)
val_df,test_df = train_test_split(temp_df,test_size = 0.5,stratify = temp_df["kredit"], random_state = 42)
print(val_df.shape)
print(test_df.shape)
print(train_df["kredit"].value_counts(normalize = True))
print(val_df["kredit"].value_counts(normalize =True))
print(test_df["kredit"].value_counts(normalize = True))

train_df.to_csv(PROJECT_ROOT / "data" / "train.csv", index=False)
val_df.to_csv(PROJECT_ROOT / "data" / "val.csv", index=False)
test_df.to_csv(PROJECT_ROOT / "data" / "test.csv", index=False)
