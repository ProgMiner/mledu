#!python3

import json
import os

import cv2
from imutils import paths


def extract_histogram(image, bins=(8, 8, 8)):
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()


def generate(path, saveY=True):
    imagePaths = sorted(list(paths.list_images(path)))
    trainData = []
    labels = []

    for i, imagePath in enumerate(imagePaths):
        image = cv2.imread(imagePath, 1)
        label = imagePath.split(os.path.sep)[-1].split(".")[0]
        hist = extract_histogram(image)
        trainData.append(hist)
        labels.append(label)

    trainData = [[str(x) for x in hist] for hist in trainData]

    if saveY:
        Y = [0 if x == 'cat' else 1 for x in labels]

        data = dict([('trainData', trainData), ('Y', Y)])
        file = open(f'{path}.json', 'w')
        json.dump(data, file)
        file.close()
    else:
        file = open(f'{path}.json', 'w')
        json.dump(dict([(imagePaths[i].split('/')[-1], hist) for i, hist in enumerate(trainData)]), file)
        file.close()


generate('train')
generate('test', False)
