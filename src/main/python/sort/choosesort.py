# -*- coding: utf-8 -*-


def choose_sort(in_list):
    arr_len = len(in_list)
    for i in range(int(arr_len / 2)):
        max_idx, min_idx = i, i
        for j in range(i, arr_len - i):
            if in_list[j] > in_list[max_idx]:
                max_idx = j
            elif in_list[j] < in_list[min_idx]:
                min_idx = j
        in_list[i], in_list[min_idx] = in_list[min_idx], in_list[i]
        in_list[arr_len - 1 - i], in_list[max_idx] = in_list[max_idx], in_list[arr_len - 1 - i]


l = [1, 45, 4, 64, 6, 5475, 7, 65, 1]
choose_sort(l)

print(l)
