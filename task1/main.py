import pandas as pd 

df = pd.read_csv("data.csv",index_col="transaction_id")

df = df.groupby("user_id").sum()

print(df)

df[["amount"]].to_csv("outut.csv")