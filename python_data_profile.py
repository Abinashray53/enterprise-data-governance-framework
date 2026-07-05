import pandas as pd

df = pd.read_csv("../data/raw/customer_master.csv")

print("\nRows :",len(df))

print("\nColumns :",len(df.columns))

print("\nData Types")

print(df.dtypes)

print("\nMissing Values")

print(df.isnull().sum())

print("\nDuplicate Records")

print(df.duplicated().sum())

print("\nSummary Statistics")

print(df.describe(include="all"))