import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="&DEC95603",
    database="risk_analysis"
)

query = """
SELECT *
FROM client_data
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df.head())

conn.close()
print(df.head(10))
