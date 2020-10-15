import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv('flights.csv')

del data['Unnamed: 36']
del data['ORIGIN_AIRPORT_SEQ_ID']
del data['DEST_AIRPORT_SEQ_ID']
del data['CRS_DEP_TIME']
del data['CRS_ARR_TIME']
del data['CRS_ELAPSED_TIME']


corrmat = data.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True,cmap=sns.diverging_palette(240, 10, n=200));
plt.show()


