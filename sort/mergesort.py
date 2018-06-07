# -*- coding: utf-8 -*-


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        div_inx = int(len(array) / 2)
        # print(array, "**********")
        return merge(merge_sort(array[:div_inx]), merge_sort(array[div_inx:]))


def merge(array1, array2):
    idx1, idx2 = 0, 0
    ret_array = []
    while idx1 < len(array1) or idx2 < len(array2):
        if idx1 == len(array1):
            ret_array += array2[idx2:]
            return ret_array
        elif idx2 == len(array2):
            ret_array += array1[idx1:]
            return ret_array

        elif array1[idx1] < array2[idx2]:
            ret_array.append(array1[idx1])
            idx1 += 1
        else:
            ret_array.append(array2[idx2])
            idx2 += 1
    return ret_array


print(merge_sort([4, 5, 9, 4,1,3]))


