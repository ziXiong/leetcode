# -*- coding: utf-8 -*-
"""
写排序算法不能随便用len(n), 一下就time exceed了。
"""


def heapify(heap, length, k):
    max_idx = length - 1
    j = k * 2 + 1
    while j < max_idx:
        if j + 1 > max_idx:
            min_idx = k * 2 + 1
        else:
            min_idx = k * 2 + 1 if heap[k * 2 + 1]['val'] < heap[k * 2 + 2]['val'] else k * 2 + 2
        if heap[k]['val'] <= heap[min_idx]['val']:
            break
        else:
            heap[k], heap[min_idx] = heap[min_idx], heap[k]
            k = min_idx

from collections import Counter
from itertools import chain

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        keys = []
        for num in nums:
            if num not in d.keys():
                d[num] = 0
                keys.append(num)
            d[num] += 1
        heap = [dict(key=key, val=d[key]) for key in keys[:k]]
        length = len(heap)

        print(d, keys)
        print(heap)
        for key in range(int((length - 2) / 2) + 1)[::-1]:
            heapify(heap, length, key)

        for key in keys[k:]:
            if d[key] > heap[0]['val']:
                heap[0] = dict(key=key, val=d[key])
                print(heap[0])
                heapify(heap, length, 0)
        return [h['key'] for h in heap]


s = Solution()
print(s.topKFrequent([11, 2, 1, 2, 4, 5, 7, 7, 6, 6, 6, 6, 9], 3))
