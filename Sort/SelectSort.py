''''
選択ソート
'''
from typing import List

def selection_sort(L: List[int]) -> List[int]:
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
    return L


nums = [2,5,6,3,8,1]
print(selection_sort(nums))

# [1, 2, 3, 5, 6, 8]