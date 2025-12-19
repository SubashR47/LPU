import pandas as pd
df=pd.read_csv(r"C:\Users\USER\Desktop\LPU\Business Analytics\creditriskdata.csv")
corr=df.corr(numeric_only=True).round(2)
print(corr.to_string())