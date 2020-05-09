from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from imutils import paths
import cv2
import os
import numpy as np
from sklearn.metrics import f1_score


def week7(rand: int, c, t0: int, t1: int, t2: int, images: list):
    def extract_histogram(image, bins=(8, 8, 8)):
        hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256,
                                                             0, 256])
        cv2.normalize(hist, hist)
        return hist.flatten()

    imagePaths = sorted(list(paths.list_images('ml/datasets/catsvsdogs/train')))
    data = []
    labels = []
    for i, imagePath in enumerate(imagePaths):

        image = cv2.imread(imagePath, 1)
        label = imagePath.split(os.path.sep)[-1].split(".")[0]
        if label == "cat":
            labels.append(0)
        if label == "dog":
            labels.append(1)
        hist = extract_histogram(image)
        data.append(hist)

    trainData, testData, trainLabels, testLabels = \
        train_test_split(np.array(data), labels,
                         test_size=0.25, random_state=int(rand))

    model = LinearSVC(random_state=int(rand), C=float(c))
    model.fit(trainData, trainLabels)

    predictions = model.predict(testData)
    a1 = round(model.coef_[0][int(t0)], 2)
    a2 = round(model.coef_[0][int(t1)], 2)
    a3 = round(model.coef_[0][int(t2)], 2)
    a4 = round(f1_score(testLabels, predictions, average='macro'), 2)

    images = images
    predictions = []
    for i in images:
        image_path = f'ml/datasets/catsvsdogs/test/{i}'
        image = cv2.imread(image_path)
        hist = extract_histogram(image).reshape(1, -1)
        prediction = model.predict(hist)
        predictions.append(prediction[0])
    a5 = predictions
    return a1, a2, a3, a4, a5
