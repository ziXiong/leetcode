# -*- coding: utf-8 -*-


def sum_zero(in_list):

    dp0, dp1, dp2 = [], [], []
    dp0[0] = 0
    if in_list[0] == 1:
        dp1[0] = 1
        dp2[0] = 0
    else:
        dp1[0] = 0
        dp2[0] = 1

    max_len = 0
    for idx in range(1, len(in_list)):
        if in_list[idx] == 1:
            dp0[idx] = dp2[idx - 1] + 1 if dp2[idx -1] != 0 else 0
            dp1[idx] = dp0[idx - 1] + 1 if dp0[idx - 1] != 0 else 0
            dp2[idx] = 1
