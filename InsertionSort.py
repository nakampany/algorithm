''''
挿入ソート
'''
from typing import List

def insertion_sort(L: List[int]) -> List[int]:
    for i in range(1, len(L)):
        temp = L[i]
        j = i - 1
        while j >= 0 and L[j] > temp:
            L[j + 1] = L[j]
            j -= 1
        
        L[j + 1] = temp

    return L


nums = [2,5,6,3,8,1]
print(insertion_sort(nums))

# [1, 2, 3, 5, 6, 8]