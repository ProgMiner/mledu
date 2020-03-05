import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


def week3(path):
    data = pd.read_csv(path, names=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    data = np.array(data)
    pca_1 = PCA(n_components=1, svd_solver='full')
    x_transformed = pca_1.fit_transform(data)
    FIRST = (round(x_transformed[0][0], 3))

    pca_2 = PCA(n_components=2, svd_solver='full')
    x_transformed = pca_2.fit_transform(data)
    SECOND = (round(x_transformed[0][1], 3))

    FIRD = (np.round(np.cumsum(pca_2.explained_variance_ratio_), 3)[1])

    pca_3 = PCA(n_components=10, svd_solver='full')
    pca_3.fit_transform(data)
    FORTH = 0
    for arg, val in enumerate(np.cumsum(pca_3.explained_variance_ratio_)):
        if val > 0.85:
            FORTH = arg + 1
            break
    fig, ax = plt.subplots()
    ax.scatter(x_transformed[:, 0], x_transformed[:, 1])
    fig.savefig('main/static/1.png')
    return FIRST, SECOND, FIRD, FORTH