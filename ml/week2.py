import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import DistanceMetric


def res(path, star):
    data = pd.read_csv(path)
    del data['TARGET']
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    mip = np.array([mip[0] for mip in scaled_data])
    mean = mip.mean()
    star = np.array(star)
    dist = DistanceMetric.get_metric('euclidean')
    distances = [dist.pairwise(np.concatenate(([i], [star])))[0][1] for i in scaled_data]
    min_distance = min(distances)
    return round(mean, 3), round(min_distance, 3)


