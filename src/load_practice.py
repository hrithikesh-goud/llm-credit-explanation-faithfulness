import pandas as pd
from pathlib import Path
PROJECT_ROOT =Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT /"data" / "SouthGermanCredit.asc" 
df=pd.read_csv(DATA_FILE,sep =r"\s+",header = 0)
print(df.shape)
print(df.head())
print(df.isnull().sum().sum())

