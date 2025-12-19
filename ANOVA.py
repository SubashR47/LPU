import pandas as pd, statsmodels.api as sm, statsmodels.formula.api as smf
df = pd.read_csv(r"C:\Users\USER\Desktop\LPU\Business Analytics\creditriskdata.csv")
print(sm.stats.anova_lm(smf.ols('loan_amnt~C(loan_status)', df).fit()))
