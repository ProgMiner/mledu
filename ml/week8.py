from math import log

from pandas import DataFrame


def week8_1(data):
    data = list(map(lambda s: s.strip().split(), data.strip().split('\n')))

    header = data[0]
    data_table = dict([(h, []) for h in header])

    data_rows = data[1:]
    for row in data_rows:
        for i in range(len(header)):
            data_table[header[i]] += [row[i]]

    data_table = DataFrame.from_dict(data_table)
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
