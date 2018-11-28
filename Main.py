import numpy as np
import pandas as pd

fname='dataset.txt'
raw_data=pd.read_csv(fname,dtype='float',delimiter='\t')
raw_data = raw_data.drop(['class'], axis=1)

centroid = 3
k = centroid

