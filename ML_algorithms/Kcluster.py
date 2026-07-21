# import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
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
# plt.figure(figsize=(8,6))

# plt.scatter(
#     df['Annual Income (k$)'],
#     df['Spending Score (1-100)']
# )

# plt.xlabel("Annual Income (k$)")
# plt.ylabel("Spending Score (1-100)")
# plt.title("Customer Distribution")

# plt.show()
# inertia=[]
# for i in range(1,11):
#     model=KMeans(n_clusters=i,random_state=42)
#     model.fit(x_scaled)
#     inertia.append(model.inertia_)
# plt.plot(range(1,11),inertia,marker='o')
# plt.show()
scores=[]
for i in range(2,11):
    model = KMeans(n_clusters=i, random_state=42)
    model.fit(x_scaled)

    score = silhouette_score(x_scaled, model.labels_)
    scores.append(score)

    print(f"K = {i}, Silhouette Score = {score:.4f}")
plt.plot(range(2,11),scores,marker='x')
plt.show()
    
