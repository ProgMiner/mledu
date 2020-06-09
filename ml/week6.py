import pandas as pd
import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier


def week6_1(spam, ham, email, words, words_to_num):
    words_to_num = words_to_num
    data = [spam, ham]
    emails = email
    words = words
    t611 = round(emails[0] / np.sum(emails), 3)
    spam_prob = math.log(emails[0] / np.sum(emails))
    spam_freq = []
    for i in words_to_num:
        if i == -1:
            spam_freq.append(1)
        else:
            spam_freq.append(data[0][i] + 1)
    spam_znam = 10 + words[0]
    for i in spam_freq:
        spam_prob += math.log(i / spam_znam)
    ham_prob = math.log(emails[1] / np.sum(emails))
    ham_freq = []
    for i in words_to_num:
        if i == -1:
            ham_freq.append(1)
        else:
            ham_freq.append(data[1][i] + 1)
    ham_znam = 10 + words[1]
    for i in ham_freq:
        ham_prob += math.log(i / ham_znam)
    spam = round(1 / (1 + math.exp(ham_prob - spam_prob)), 3)
    t612 = (round(spam_prob, 3))
    t613 = (round(ham_prob, 3))
    t614 = spam
    return t611, t612, t613, t614


def week6_2(x_0, y_0, cl, obj):
    data = [x_0, y_0, cl]
    Data = pd.DataFrame(data=np.array(data).transpose()
                        , index=range(1, 11))
    X = pd.DataFrame(Data.drop([2], axis=1))
    y = np.array(data[2])
    Clf = KNeighborsClassifier(n_neighbors=3, p=2)
    Clf.fit(X, y)
    Obj_1 = np.array(obj).reshape(1, 2)
    t621 = round(Clf.kneighbors(Obj_1)[0][0][0], 3)
    t622 = [i + 1 for i in Clf.kneighbors(Obj_1)[1][0]]
    t623 = Clf.predict(Obj_1)[0]
    Clf_2 = KNeighborsClassifier(n_neighbors=3, p=1)
    Clf_2.fit(X, y)
    t624 = round(Clf_2.kneighbors(Obj_1)[0][0][0], 3)
    t625 = [i + 1 for i in Clf_2.kneighbors(Obj_1)[1][0]]
    t626 = Clf_2.predict(Obj_1)[0]
    return t621, t622, t623, t624, t625, t626
