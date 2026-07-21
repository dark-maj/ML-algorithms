import numpy as np
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

res=load_digits()
X=res.data
y=res.target
print(X.shape)
print(y.shape)
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X[i].reshape(8,8),cmap='gray')
    plt.title(f"label:{y[i]}")
    plt.axis('off')


plt.show()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# print(X_train.shape)
# print(y_train.shape)
# print(X_test.shape)
# print(y_test.shape)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
x=knn.predict(X_test)
# print(x[:10])
# print(y_test[:10])
knn.score(X_test,y_test)
cm=confusion_matrix(y_test,x)

accuracy=[]
k_values=[]
for k in range(1,20):
    knn=KNeighborsClassifier(k)
    knn.fit(X_train,y_train)
    x=knn.predict(X_test)
# print(x[:10])
# print(y_test[:10])
    l=knn.score(X_test,y_test)
    k_values.append(k)
    accuracy.append(l)
ConfusionMatrixDisplay(cm).plot()  
plt.figure() 
plt.plot(k_values,accuracy)
plt.show()





