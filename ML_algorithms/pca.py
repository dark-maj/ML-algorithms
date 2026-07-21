import pandas as pd
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
d=load_wine()
df=pd.DataFrame(d.data,columns=d.feature_names)
df['target']=d.target
X=d.data
y=d.target
print(X.shape)

print(df.describe())
corr=df.drop('target',axis=1).corr()
plt.figure(figsize=(8,6))
plt.imshow(corr,cmap='coolwarm',vmin=-1,vmax=1)
plt.colorbar()
plt.xticks(range(len(corr.columns)),corr.columns,rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Feature Correlation Heatmap")
plt.show()

