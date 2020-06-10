from ml.datasets import catsvsdogs


def week10(C, random_state, criterion, min_samples_leaf, max_leaf_samples, n_estimators, solver, cv, clazz, images):
    trainData, Y = catsvsdogs.train
    Y = [(y + 1) % 2 for y in Y]

    from sklearn.ensemble import BaggingClassifier
    from sklearn.tree import DecisionTreeClassifier

    tree = DecisionTreeClassifier(criterion=criterion,  # критерий разделения
                                  min_samples_leaf=min_samples_leaf,  # минимальное число объектов в листе
                                  max_leaf_nodes=max_leaf_samples,  # максимальное число листьев
                                  random_state=random_state)
    bagging = BaggingClassifier(tree,  # базовый алгоритм
                                n_estimators=n_estimators,  # количество деревьев
                                random_state=random_state)
    bagging.fit(trainData, Y)

    from sklearn.svm import LinearSVC

    svm = LinearSVC(random_state=random_state, C=C)
    svm.fit(trainData, Y)

    from sklearn.ensemble import RandomForestClassifier

    forest = RandomForestClassifier(n_estimators=n_estimators,  # количество деревьев
                                    criterion=criterion,  # критерий разделения
                                    min_samples_leaf=min_samples_leaf,  # минимальное число объектов в листе
                                    max_leaf_nodes=max_leaf_samples,  # максимальное число листьев
                                    random_state=random_state)
    forest.fit(trainData, Y)

    from sklearn.linear_model import LogisticRegression

    lr = LogisticRegression(solver=solver, random_state=random_state)

    from sklearn.ensemble import StackingClassifier

    base_estimators = [('SVM', svm), ('Bagging DT', bagging), ('DecisionForest', forest)]
    sclf = StackingClassifier(estimators=base_estimators, final_estimator=lr, cv=cv)
    sclf.fit(trainData, Y)

    accuracy = sclf.score(trainData, Y)

    probas = []
    for img in images:
        histt = catsvsdogs.test[img].reshape(1, -1)
        probas += [(img, sclf.predict_proba(histt)[0][clazz])]

    return {'accuracy': accuracy, 'probas': probas}
