from numpy import linalg as LA


def week11(pi, P, R, gamma):
    b = [0 for _ in range(0, 4)]

    A = []
    for i in range(0, 4):
        A.append([0 for _ in range(0, 4)])
        A[i][i] = 1

    for s_1 in range(0, 4):
        for a in range(0, 3):
            if a not in P[s_1]:
                continue

            for s_2 in range(0, 4):
                if s_2 not in P[s_1][a]:
                    continue

                A[s_1][s_2] += -gamma * pi[s_1][a] * P[s_1][a][s_2]
                b[s_1] += pi[s_1][a] * P[s_1][a][s_2] * R[s_1][a][s_2]

    x = LA.solve(A, b)
    return {'solution': [(i + 1, x) for i, x in enumerate(x)]}
