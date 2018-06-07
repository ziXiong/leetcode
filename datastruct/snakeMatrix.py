# -*- coding: utf-8 -*-


def snake_matrix(n):
    m = [[0 for _ in range(n)] for _ in range(n)]

    i, j = 0, 0
    m[i][j] = 1
    t = 2

    while m[i][j + 1] == 0:

        while j + 1 < n and m[i][j + 1] == 0:
            j += 1
            m[i][j] = t
            t += 1
        while i + 1 < n and m[i + 1][j] == 0:
            i += 1
            m[i][j] = t
            t += 1
        while j - 1 >= 0 and m[i][j - 1] == 0:
            j -= 1
            m[i][j] = t
            t += 1
        while i - 1 >= 0 and m[i - 1][j] == 0:
            i -= 1
            m[i][j] = t
            t += 1
    return m

import time
s = time.time()
snake_matrix(10000)
print(time.time() - s)
