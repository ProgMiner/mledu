from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


def test_alg(rd_state=42):
    X, y = load_iris(return_X_y=True)
    clf = DecisionTreeClassifier(random_state=rd_state)
    data = cross_val_score(clf, X, y, cv=5)
    return data


