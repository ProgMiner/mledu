import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


def week5(path, path2, dc1, dc2, dc3, candy1, candy2):
    data = pd.read_csv(path, index_col='competitorname')
    train_data = data.drop([dc1, dc2, dc3])
    X = pd.DataFrame(train_data.drop(['winpercent', 'Y'], axis=1))
    y = pd.DataFrame(train_data['Y'])
    reg = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y.values.ravel())
    test = pd.read_csv(path2, index_col='competitorname')
    X_test = pd.DataFrame(test.drop(['Y'], axis=1))
    first_candy = X_test.loc[candy1, :].to_frame().T
    FIRST = round(reg.predict_proba(first_candy)[0][1], 3)
    second_candy = X_test.loc[candy2, :].to_frame().T
    SECOND = round(reg.predict_proba(second_candy)[0][1], 3)
    y_pred = reg.predict(X_test)
    Y_true = test['Y'].to_frame().T.values.ravel()
    THIRD = round(metrics.recall_score(Y_true, y_pred), 3)
    FORTH = round(metrics.precision_score(Y_true, y_pred), 3)
    fpr, tpr, thresholds = metrics.roc_curve(Y_true, y_pred)
    FITH = round(metrics.auc(fpr, tpr), 3)
    return FIRST, SECOND, THIRD, FORTH, FITH
