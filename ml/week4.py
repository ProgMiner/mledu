import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def week_4_1(path_1, ):
    data = pd.read_csv(path_1)
    lr = LinearRegression()
    task_1 = data['X'].mean()
    task_2 = data['Y'].mean()  # среднее по Y
    x = np.array(data['X']).reshape(-1, 1)
    y = np.array(data['Y']).reshape(-1, 1)
    lr.fit(x, y)
    task_4 = round(lr.intercept_[0], 3)
    task_3 = round(lr.coef_[0][0], 3)
    predict = lr.predict(x)
    task_5 = round(r2_score(y, predict), 3)
    return task_1, task_2, task_3, task_4, task_5


def week4_2(path_2, candy_1, candy_2, array):
    lr = LinearRegression()
    data_candy = pd.read_csv(path_2, index_col='competitorname')
    X_candy = data_candy.drop([candy_1, candy_2])
    Y_candy = X_candy['winpercent']
    del X_candy['winpercent']
    del X_candy['Y']
    del data_candy['winpercent']
    del data_candy['Y']
    data_candy_1 = np.array(data_candy.loc[candy_1]).reshape(1, -1)
    data_candy_2 = np.array(data_candy.loc[candy_2]).reshape(1, -1)
    X_candy = np.array(X_candy)
    lr.fit(X_candy, Y_candy)
    task_6 = round(lr.predict(data_candy_1)[0], 3)
    task_7 = round(lr.predict(data_candy_2)[0], 3)
    array = np.array([array]).reshape(1, -1)
    task_8 = round(lr.predict(array)[0], 3)
    return task_6, task_7, task_8
