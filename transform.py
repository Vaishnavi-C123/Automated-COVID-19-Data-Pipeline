import pandas as pd

df = pd.read_csv("covid_data.csv")

df = df[['country', 'cases', 'deaths', 'recovered']]

df['recovery_rate'] = (df['recovered'] / df['cases']) * 100

print(df.head())
df.to_csv("transformed_covid_data.csv", index=False)

print("Transformation Completed Successfully")