from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


class Test:
    def __init__(self):
        self.data = 42

    def test_alg(self):
        X, y = load_iris(return_X_y=True)
        clf = DecisionTreeClassifier(random_state=self.data)
        data = cross_val_score(clf, X, y, cv=5)
        return data



