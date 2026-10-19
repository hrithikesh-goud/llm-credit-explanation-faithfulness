import pandas as pd

df = pd.read_csv(r"C:\Users\manthuri hrithikesh\Desktop\ML Project- CA\data\SouthGermanCredit.asc", sep=" ")
print("Rows, columns:", df.shape)
print(df["kredit"].value_counts())
print(df.isnull().sum().sum(), "missing values")