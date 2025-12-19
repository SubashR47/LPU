import pandas as pd, statsmodels.api as sm
df=pd.read_csv(r"C:\Users\USER\Desktop\LPU\Business Analytics\creditriskdata.csv")
X=sm.add_constant(df.select_dtypes("number").drop(columns="loan_amnt"))
y=df["loan_amnt"]
print(sm.OLS(y,X,missing="drop").fit().params) 