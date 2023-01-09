import pandas as pd

df = pd.DataFrame()

df["date"] = pd.date_range("1/12/2022", periods=100000, freq="H")

df = df.set_index(df["date"])

print(df.loc["2022-12-13 01:00:00":"2022-12-14 01:00:00"])



