import pandas as pd

df = pd.read_csv("data.csv")

df = df.replace(r'\n\n',' ', regex=True)

df.to_csv("newdata.csv")