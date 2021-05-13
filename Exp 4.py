# Encode the dependent variable and then split dataset into train and test set

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
Y=le.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,
random_state=1)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)