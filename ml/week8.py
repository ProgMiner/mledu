from math import log

import pandas as pd


def week8_1(data):
    data = list(map(lambda s: s.strip().split(), data.strip().split('\n')))

    header = data[0]
    data_table = dict([(h, []) for h in header])

    data_rows = data[1:]
    for row in data_rows:
        for i in range(len(header)):
            data_table[header[i]] += [row[i]]

    data_table = pd.DataFrame.from_dict(data_table)
    data_table_rows = list(map(lambda a: dict(a), map(lambda a: a[1], data_table.iterrows())))

    demand_list = list(data_table['Demand'])
    p_demand_yes = sum(map(lambda s: s == 'Yes', demand_list)) / len(demand_list)
    p_demand_no = 1 - p_demand_yes

    h_demand = -sum(map(lambda x: x * log(x, 2), [p_demand_yes, p_demand_no]))

    p_demand_cond = []
    for food in dict(map(lambda x: (x, 0), data_table['Food'])).keys():
        count = len(list(filter(lambda s: s == food, data_table['Food'])))
        yes_count = len(list(filter(lambda r: r['Food'] == food and r['Demand'] == 'Yes', data_table_rows)))
        p_demand_cond += [(food, {'Yes': f'{yes_count}/{count}', 'No': f'{count - yes_count}/{count}'})]

    ig_demand_param = []
    h_demand_cond = []
    for param in list(filter(lambda p: p != 'Demand', list(data_table))):
        h_demand_param_cond = []

        h_full = 0
        for value in dict(map(lambda x: (x, 0), data_table[param])).keys():
            count = len(list(filter(lambda s: s == value, data_table[param])))
            yes_count = len(list(filter(lambda r: r[param] == value and r['Demand'] == 'Yes', data_table_rows)))

            p_yes = yes_count / count
            p_no = (count - yes_count) / count
            h = -sum(map(lambda p: p * log(p, 2), [p_yes, p_no]))
            h_demand_param_cond += [(value, h)]

            h_full += h * count / len(data_rows)

        h_demand_cond += [(param, h_demand_param_cond)]
        ig_demand_param += [(param, h_demand - h_full)]

    return {'data': str(data),
            'h_demand': h_demand,
            'p_demand_cond': p_demand_cond,
            'h_demand_food_cond': list(filter(lambda a: a[0] == 'Food', h_demand_cond))[0][1],
            'ig_demand_param': ig_demand_param}


def week8_2(count, train_part, criterion, max_leaf_nodes, min_samples_leaf, random_state, patients):
    df = pd.read_csv('ml/diabetes.csv')
    task_data = df.head(count)

    not_ill_count = len(task_data[task_data['Outcome'] == 0])
    ill_count = len(task_data[task_data['Outcome'] == 1])

    train_part = int(len(task_data) * train_part / 100)
    train = task_data.head(train_part)
    test = task_data.tail(len(task_data) - train_part)

    features = list(train.columns[:8])
    x = train[features]
    y = train['Outcome']

    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion=criterion,  # критерий разделения
                                  min_samples_leaf=min_samples_leaf,  # минимальное число объектов в листе
                                  max_leaf_nodes=max_leaf_nodes,  # максимальное число листьев
                                  random_state=random_state)
    clf = tree.fit(x, y)

    depth = clf.tree_.max_depth

    def dfs(i=0, d=1):
        if clf.tree_.children_left[i] <= i and clf.tree_.children_right[i] <= i:
            return None

        if d == depth:
            return clf.tree_.feature[i], clf.tree_.threshold[i]

        left = dfs(clf.tree_.children_left[i], d + 1)
        right = dfs(clf.tree_.children_right[i], d + 1)

        if left is None:
            return right
        else:
            return left

    last_predictor = dfs()
    last_predictor = (list(x)[last_predictor[0]], last_predictor[1])

    features = list(test.columns[:8])
    x = test[features]
    y_true = test['Outcome']
    y_pred = clf.predict(x)

    from sklearn.metrics import accuracy_score
    accuracy_score = accuracy_score(y_true, y_pred)

    from sklearn.metrics import f1_score
    f1_score = f1_score(y_true, y_pred, average='macro')

    patients = [int(i.strip()) for i in patients.split(',')]
    prediction = [clf.predict([df.loc[i, features].tolist()])[0] for i in patients]
    prediction = [(p, prediction[i]) for i, p in enumerate(patients)]

    return {'not_ill_count': not_ill_count, 'ill_count': ill_count, 'depth': depth,
            'last_predictor': last_predictor[0], 'last_predictor_value': last_predictor[1],
            'accuracy_score': accuracy_score, 'f1_score': f1_score, 'prediction': prediction}
