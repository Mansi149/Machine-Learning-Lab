# importing dataset and selecting columns)

import pandas as pd
dataset=pd.read_csv("Data.csv")
X=dataset.iloc[:,0:1].values
Y=dataset.iloc[:,1:2].values
Z=dataset.iloc[:,2:3].values

