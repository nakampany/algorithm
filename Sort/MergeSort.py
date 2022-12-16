''''
マージソート
'''
from typing import List

def merge_sort(L: List[int]) -> List[int]:
    if len(L) <= 1:
        return L
    
    center = len(L) // 2
    left = L[:center]
    right = L[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            L[k] = left[i]
            i += 1
        else:
            L[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        L[k] = left[i]
        i += 1
        k += 1
    
    while i < len(right):
        L[k] = right[j]
        j += 1
        k += 
        
    return L




nums = [2,5,6,3,8,1]
print(merge_sort(nums))