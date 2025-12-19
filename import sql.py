import psycopg2, pandas as pd
conn=psycopg2.connect(
    host="localhost", port="5432",
    dbname="creditriskdb", user="postgres", password="Suba@5680"
)

df=pd.read_sql("SELECT * FROM public.creditriskdata;",conn)
print(df)
conn.close()