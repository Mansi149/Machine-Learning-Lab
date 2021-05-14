# Implement Simple Linear Regression Model.

import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv:)
X = dataset.iloc[:,0:1].values
y = dataset.iloc[:,1:2].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = &#39;red&#39;)
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title(&#39;Salary vs Experience (Training set)&#39;)

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()