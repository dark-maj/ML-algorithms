import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("data/Mall_Customers.csv")
X=df[['Age','Annual Income (k$)','Spending Score (1-100)']]
scaler=StandardScaler()
x_scaled=scaler.fit_transform(X)
scaled_df = pd.DataFrame(
    x_scaled,
    columns=['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
)
print(x_scaled[:5])
print(scaled_df.describe())
print(df.describe())
print(df.head())
plt.figure(figsize=(8,6))

plt.scatter(
    df['Annual Income (k$)'],
    df['Spending Score (1-100)']
)

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Distribution")

plt.show()