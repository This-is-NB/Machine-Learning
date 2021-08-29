import pandas as pd
data = pd.read_csv("salary.csv")
data
data.head()
data.info()
x = data["YearsExperience"]
type(x)
x=x.values
type(x)
x=x.reshape(-1,1)  # -1 will take the len of record. 
x.shape
y = data["Salary"]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
model.coef_
model.predict([[2.5]])
manual_pred = model.coef_ * 2.5
print(manual_pred)
model_pred = model.predict([[2.5]])
print(model_pred)
model.intercept_
pred = model.coef_ * 2.5 + model.intercept_
print(pred)





