import pandas as pd, numpy as np
df=pd.read_csv(r"C:\Users\USER\Desktop\LPU\Business Analytics\creditriskdata.csv")
num=df.select_dtypes(include=[np.number])
d=num.describe()
print(d)
