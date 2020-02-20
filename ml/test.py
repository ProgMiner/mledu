from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
X, y = load_iris()
clf = DecisionTreeClassifier(random_state=42)
data = cross_val_score(clf, X, y, cv=5)


