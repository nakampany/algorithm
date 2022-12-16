
''''
バブルソート
'''
from typing import List

def bubble_sort(L: List[int]) -> List[int]:
    for i in range(len(L)):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


nums = [2,5,6,3,8,1]
print(bubble_sort(nums))

# [1, 2, 3, 5, 6, 8]