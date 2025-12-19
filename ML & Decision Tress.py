import subprocess, sys
for pkg in ['pandas','scikit-learn','matplotlib']:
    try:
        __import__(pkg.replace('-', '_'))
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\USER\Desktop\LPU\Business Analytics\creditriskdata.csv")
num_df = df.select_dtypes(include='number')
target = df['loan_status'] if 'loan_status' in df.columns else df.iloc[:, -1]
X = num_df.drop(columns=['loan_status'], errors='ignore')

X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train, y_train)

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, model.predict(X_test)))

plt.figure(figsize=(12, 6))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=[str(c) for c in sorted(target.unique())],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.show()
