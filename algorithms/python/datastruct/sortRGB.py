# -*- coding: utf-8 -*-


def sort_rgb(in_list):
    length = len(in_list)
    r_idx, b_idx = 0, length - 1
    idx = 0
    while idx < b_idx:
        if in_list[idx] == 'R':
            in_list[r_idx], in_list[idx] = in_list[idx], in_list[r_idx]
            r_idx += 1
            idx += 1
        elif in_list[idx] == 'G':
            idx += 1
        else:
            in_list[b_idx], in_list[idx] = in_list[idx], in_list[b_idx]
            b_idx -= 1

in_list = list('RBGRBGBRRGBGRGGRGBGRGBGRGRBGGRGGB')
sort_rgb(in_list)
print(in_list)
