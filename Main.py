import numpy as np
import pandas as pd
import random as rand
from tqdm import tqdm

def manhattan_distance(comparison, k):
    temp=0.0
    for iter in range(0, 7):
        temp = temp + np.absolute(raw_data.loc[comparison,:].values.tolist()[iter] - centroid_point.loc[k,:].values.tolist()[iter])
    return temp        

fname='dataset.txt'
"""
Setting-Up DataFrame for main data storage
"""
raw_data=pd.read_csv(fname,dtype='float',delimiter='\t')
raw_data = raw_data.drop(['class'], axis=1)

"""
Setting-Up DataFrame for CRUD 'centroid-data' Table Distance
"""
df = pd.DataFrame(np.random.randn(210, 4), index=None, columns=None)
temp1=0

"""
Setting-Up K-centroid and DataFrame for centroid
"""
centroid = 3
k = list()
cluster=[float(pt) for pt in range(0,centroid)]
centroid_point = raw_data.head(centroid)
for i in range(0, centroid):
    k.append(rand.randrange(1,210,1))
for properties in raw_data.columns.tolist():
    for z in range(0,len(cluster)):
        centroid_point.loc[cluster[z]][properties] = raw_data.loc[k[z]][properties]

"""
Algorithm Begins
"""
for iteration in tqdm(range(0,50)): #iteration to gain optimum value
    for j in range(0,210):
        thisdict = {0:66,1:66,2:66}
        for i in range(0, centroid):
            temp1 = manhattan_distance(j, i)
            thisdict[i]=temp1
            df[i][j] = temp1
        df[3][j]=min(thisdict.items(), key=lambda x: x[1])[0]
    for properties in raw_data.columns.tolist():
        for z in cluster:
            centroid_point.loc[int(z)][properties] = np.mean([raw_data.loc[x][properties].tolist() for x in df.loc[df[3]==z].index.tolist()])
        
            





