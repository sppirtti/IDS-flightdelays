import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import abline_plot
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn import metrics 
from scipy.spatial.distance import cdist 


data = pd.read_csv('flights.csv')
data=data.fillna(0)

clus = data.ARR_DELAY.values
clus1 = data.DISTANCE.values

clus = np.vstack((clus1, clus)).T

model = KMeans(4)
model.fit(clus)
plt.scatter(clus[:,0],clus[:,1], c=model.labels_)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], s=100, color="red"); # Show the centres
plt.xlabel("Distance")
plt.ylabel("Arrival delay")
plt.show()

distortions = [] 
inertias = [] 
mapping1 = {} 
mapping2 = {} 
K = range(1,10) 
  
for k in K: 
    kmeanModel = KMeans(n_clusters=k).fit(clus) 
    kmeanModel.fit(clus)     
      
    distortions.append(sum(np.min(cdist(clus, kmeanModel.cluster_centers_, 
                      'euclidean'),axis=1)) / clus.shape[0]) 
    inertias.append(kmeanModel.inertia_) 
  
    mapping1[k] = sum(np.min(cdist(clus, kmeanModel.cluster_centers_, 
                 'euclidean'),axis=1)) / clus.shape[0] 
    mapping2[k] = kmeanModel.inertia_ 

plt.plot(K, distortions, 'bx-') 
plt.xlabel('Values of K') 
plt.ylabel('Distortion') 
plt.title('The Elbow Method using Distortion') 
plt.show() 

plt.plot(K, inertias, 'bx-') 
plt.xlabel('Values of K') 
plt.ylabel('Inertia') 
plt.title('The Elbow Method using Inertia') 
plt.show() 

#optimal number of clusters is 4
