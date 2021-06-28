import pandas as pd

df = pd.read_csv('https://bit.ly/ds-house-price')

df = df.rename(columns={'분양가격(㎡)': '분양가격'})

print(df.head())