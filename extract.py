import requests
import pandas as pd

url = "https://disease.sh/v3/covid-19/countries"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

print(df[['country', 'cases', 'deaths', 'recovered']].head())
df.to_csv("covid_data.csv", index=False)

print("CSV File Created Successfully")