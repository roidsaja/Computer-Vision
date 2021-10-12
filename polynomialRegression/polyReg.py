from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.pipeline import make_pipeline

dataset = pd.read_csv('time_series_covid19_confirmed_global.csv')
cases = []
columns = dataset.keys()
confirmed = dataset.iloc[:, 4:777]
confirmed_dates = confirmed.keys()

for i in confirmed_dates:
    confirmed_sum = confirmed[i].sum()
    cases.append(confirmed_sum)

day_initial = np.array( [i for i in range(len(confirmed_dates)) ]).reshape(-1, 1)
cases = np.array(cases).reshape(-1, 1)

future_day = 20
future_predict = np.array( [i for i in range(len(confirmed_dates) + future_day) ]).reshape(-1, 1)
#print(future_predict)
dates_adjust = future_predict[:-future_day]
#print(dates_adjust)

start = '1/22/2020'
date_start = datetime.datetime.strptime(start, '%m/%d/%Y')
date_future = []
for i in range(len(future_predict)):
    date_future.append( (date_start + datetime.timedelta(days = i)).strftime('%m/%d/%Y'))
#print(date_future)

# set test_size to 15% of the original data, set shuffle to False since the model needs to learn from the trend of the data
X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(day_initial, cases, test_size=0.15, shuffle=False)

# transform data for polynomial regression
poly = PolynomialFeatures(degree=5)
poly_X_train_confirmed = poly.fit_transform(X_train_confirmed)
poly_X_test_confirmed = poly.fit_transform(X_test_confirmed)
polyPredictFuture = poly.fit_transform(future_predict)

# polynomial regression
lm = LinearRegression(normalize=True, fit_intercept=True)
lm.fit(poly_X_train_confirmed, y_train_confirmed)
testLinearPredict = lm.predict(poly_X_test_confirmed)
linearPredict = lm.predict(polyPredictFuture)
print('MAE:', mean_absolute_error(testLinearPredict, y_test_confirmed))
print('MSE', mean_squared_error(testLinearPredict, y_test_confirmed))

plt.plot(testLinearPredict)
plt.plot(y_test_confirmed)
plt.legend(['Confirmed Cases', 'Linear Prediction'], prop={'size':10})
plt.show()