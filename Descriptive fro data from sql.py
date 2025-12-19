import pandas as pd
import numpy as np
import psycopg2
conn=psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="creditriskdb",
    user="postgres",
    password="Suba@5680"
)
df=pd.read_sql("SELECT * FROM public.creditriskdata;", conn)
num=df.select_dtypes(include=[np.number])
d=num.describe()
print(d)
conn.close()