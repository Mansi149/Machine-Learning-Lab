# Encode categorical data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',
OneHotEncoder(),[0])],
remainder='passthrough')
X=np.array(ct.fit_transform(X))
print(X)