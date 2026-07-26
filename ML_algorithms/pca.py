import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
d=load_wine()
df=pd.DataFrame(d.data,columns=d.feature_names)
df['target']=d.target
X=d.data
y=d.target
print(X.shape)

# print(df.describe())
# corr=df.drop('target',axis=1).corr()
# plt.figure(figsize=(8,6))
# plt.imshow(corr,cmap='coolwarm',vmin=-1,vmax=1)
# plt.colorbar()
# plt.xticks(range(len(corr.columns)),corr.columns,rotation=90)
# plt.yticks(range(len(corr.columns)), corr.columns)
# plt.title("Feature Correlation Heatmap")
# plt.show()
# print(df['proline'].var())
# print(df['hue'].var())
scaler=StandardScaler()
x_scaled=scaler.fit_transform(X)
# print(x_scaled)
pca=PCA()
pca.fit(x_scaled)
print(pca.explained_variance_ratio_)
cum_var=pca.explained_variance_ratio_.cumsum()
plt.plot(range(1, 14), cum_var)
plt.axhline(y=0.95, color='r', linestyle='--', label='95% variance')
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.title('Scree Plot (Cumulative)')
plt.legend()
plt.show()

# Choosing number of components: smallest n where cumulative variance >= 95%
n_components=int((cum_var >= 0.95).argmax() + 1)
print(f"Components needed for 95% variance: {n_components}")

# --- 2D projection colored by class ---
pca_2d=PCA(n_components=2)
X_pca_2d=pca_2d.fit_transform(x_scaled)

plt.figure(figsize=(8,6))
scatter=plt.scatter(X_pca_2d[:,0], X_pca_2d[:,1], c=y, cmap='viridis', edgecolor='k')
plt.xlabel(f"PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% var)")
plt.ylabel(f"PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% var)")
plt.title("Wine dataset projected onto first 2 principal components")
plt.legend(handles=scatter.legend_elements()[0], labels=list(d.target_names))
plt.show()

# --- Compare separability vs. two raw features (unscaled feature-pair baseline) ---
plt.figure(figsize=(8,6))
scatter2=plt.scatter(df['flavanoids'], df['color_intensity'], c=y, cmap='viridis', edgecolor='k')
plt.xlabel('flavanoids')
plt.ylabel('color_intensity')
plt.title('Raw feature pair (for comparison to PCA projection)')
plt.legend(handles=scatter2.legend_elements()[0], labels=list(d.target_names))
plt.show()

# --- Interpret PC1 / PC2 loadings ---
loadings=pd.DataFrame(
    pca_2d.components_.T,
    columns=['PC1','PC2'],
    index=d.feature_names
)
print("\nTop features driving PC1:")
print(loadings['PC1'].abs().sort_values(ascending=False).head(5))
print("\nTop features driving PC2:")
print(loadings['PC2'].abs().sort_values(ascending=False).head(5))

# --- PCA limitations (notes, not code) ---
# 1. Linear only: PCA finds linear combinations of features: it can't capture
#    curved/non-linear structure the way manifold methods can.
# 2. Scale-sensitive: features with larger variance dominate components unless
#    you standardize first (this is why StandardScaler ran before PCA above).
# 3. Loses interpretability: PC1/PC2 are blends of original features, so
#    "what does this axis mean" requires inspecting loadings, unlike a raw feature.
# 4. Global variance-preserving, not class-aware: PCA doesn't know about labels,
#    so it maximizes variance, not class separability (LDA optimizes for that).

# --- PCA vs t-SNE / UMAP ---
# PCA: linear, deterministic, fast, preserves global variance structure,
#   axes are interpretable (loadings), good first pass / preprocessing step.
# t-SNE/UMAP: non-linear, stochastic (t-SNE) or approx-deterministic (UMAP),
#   optimize to preserve local neighborhood structure, better for visualizing
#   tight non-linear clusters, but axes have no interpretable meaning and
#   distances between distant clusters aren't meaningful.

