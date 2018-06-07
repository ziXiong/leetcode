# -*- coding: utf-8 -*-


lcs_str = []


def lcs(a, b, m, n):
    if m < 0 or n < 0:
        return 0
    elif a[m] == b[n]:
        lcs_str.append(a[m])
        return 1 + lcs(a, b, m - 1, n - 1)
    else:
        return max(lcs(a, b, m - 1, n), lcs(a, b, m, n - 1))

a = 'cdajflkdalf'
b = 'aeoobdellf'
print(lcs(a, b, len(a) - 1, len(b) - 1))

