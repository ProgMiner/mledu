import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


def week9(csv, x_1, y_1, x_2, y_2, x_3, y_3):
    data = pd.read_csv(csv, delimiter=',', index_col='Object')
    coords = data.drop('Cluster', axis=1)
    centroid = np.array([[x_1, y_1], [x_2, y_2], [x_3, y_3]])
    kmeans = KMeans(n_clusters=3, init=centroid, max_iter=100, n_init=1)

    model = kmeans.fit(coords)
    answers = model.labels_.tolist()
    dist = kmeans.fit_transform(coords)

    my_claster = []

    for i in range(len(dist)):
        if answers[i] == 0:
            my_claster.append(dist[i][0].tolist())

    return answers, round(np.mean(my_claster), 3)
