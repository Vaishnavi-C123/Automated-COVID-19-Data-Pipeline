import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    database="covid_db",
    user="postgres",
    password="postgres123",
    host="localhost",
    port="5432"
)

# Read transformed CSV file
df = pd.read_csv("transformed_covid_data.csv")

# Create cursor
cur = conn.cursor()
for _, row in df.iterrows():

    cur.execute(
        """
        INSERT INTO covid_stats
        (country, cases, deaths, recovered, recovery_rate)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            str(row['country']),
            int(row['cases']),
            int(row['deaths']),
            int(row['recovered']),
            float(row['recovery_rate'])
        )
    )

conn.commit()

print("All Rows Inserted Successfully")

# Close connection
cur.close()
conn.close()