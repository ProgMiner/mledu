import json

from numpy import float32, array


def load(path, loadY=True):
    file = open(f'ml/datasets/catsvsdogs/{path}.json', 'r')
    data = json.load(file)
    file.close()

    if loadY:
        trainData = [array([float32(x) for x in hist]) for hist in data['trainData']]
        return trainData, data['Y']
    else:
        for name, hist in data.items():
            data[name] = array([float32(x) for x in hist])

        return data


train = load('train')
test = load('test', False)
