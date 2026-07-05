import random
import pandas as pd
from faker import Faker
import os

fake = Faker()

os.makedirs("../data/raw", exist_ok=True)

cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Hyderabad",
    "Kolkata",
    "Chennai"
]

departments = [
    "Finance",
    "Sales",
    "HR",
    "IT",
    "Operations"
]

records = []

for i in range(1000):

    records.append({

        "Customer_ID": i + 1,

        "Name": fake.name(),

        "Age": random.randint(18,65),

        "City": random.choice(cities),

        "Department": random.choice(departments),

        "Salary": random.randint(25000,150000),

        "Email": fake.email()

    })

df = pd.DataFrame(records)

df.loc[5,"Email"] = None
df.loc[12,"Salary"] = None

duplicate = df.iloc[25]

df = pd.concat(
    [df,pd.DataFrame([duplicate])],
    ignore_index=True
)

df.to_csv("../data/raw/customer_master.csv",index=False)

print(df.head())

print("\nDataset Generated Successfully")
