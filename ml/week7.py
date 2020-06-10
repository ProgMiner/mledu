import numpy as np
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

from ml.datasets import catsvsdogs


def week7(rand: int, c, t0: int, t1: int, t2: int, images: list):
    data, labels = catsvsdogs.train

    trainData, testData, trainLabels, testLabels = train_test_split(np.array(data), labels, test_size=0.25,
                                                                    random_state=int(rand))

    model = LinearSVC(random_state=int(rand), C=float(c))
    model.fit(trainData, trainLabels)

    predictions = model.predict(testData)
    a1 = round(model.coef_[0][int(t0)], 2)
    a2 = round(model.coef_[0][int(t1)], 2)
    a3 = round(model.coef_[0][int(t2)], 2)
    a4 = round(f1_score(testLabels, predictions, average='macro'), 2)

    predictions = []
    for i in images:
        hist = catsvsdogs.test[i].reshape(1, -1)
        prediction = model.predict(hist)
        predictions.append(prediction[0])
    a5 = predictions
    return a1, a2, a3, a4, a5
