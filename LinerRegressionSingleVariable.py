import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn import linear_model

df = pd.read_csv("homeprices.csv")
# [Not valid for Pycharm] %matplotlib inline


reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)
print reg.predict([[3300]])
print reg.coef_
print reg.intercept_
print type(reg.coef_)
#y = reg.coef_* [3300]) + reg.intercept_
#print ('price of the house will be: ',y)
dArea = pd.read_csv("areas.csv")
price = reg.predict(dArea)
dArea['prices'] = price
dArea.to_csv("prediction.csv", index = False)
plt.xlabel('Area (sqr feet)')
plt.ylabel('Price (US $)')
plt.scatter(df.area, df.price, color ='red', marker='^')
print plt.plot(df.area, reg.predict(df[['area']]),color ='yellow')
plt.interactive(False)
plt.show(block=True)
