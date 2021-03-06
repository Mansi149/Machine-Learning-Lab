# Implement Polynomial Regression Model

import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Position_Salaries'.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

#Training the Linear Regression model on the whole dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#Training the Polynomial Regression model on the whole dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#Visualising the Linear Regression results
plt.scatter(X, y, color = &#39;red&#39;)
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title(&#39;Truth or Bluff (Linear Regression)&#39;)

plt.xlabel(&#39;Position Level&#39;)
plt.ylabel(&#39;Salary&#39;)
plt.show()

#Visualising the Polynomial Regression results
plt.scatter(X, y, color = &#39;red&#39;)
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Predicting a new result with Linear Regression
lin_reg.predict([[6.5]])
# single bracket of 6.5 creates list, thtsy double for array
array([330378.78787879])

#Predicting a new result with Polynomial Regression¬∂
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
array([158862.45265153])