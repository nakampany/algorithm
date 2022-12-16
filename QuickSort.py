''''
クイックソート
'''
from typing import List

def partition(L: List[int], low: int, high:int) -> int:
    i = low -1
    pivot = L[high]
    for j in range(low, high):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    return i + 1


def quick_sort(L: List[int]) -> List[int]:
    def _quick_sort(L: List[int], low: int, high:int) -> None:
        if low < high:
            partition_index = partition(L, low, high)
            _quick_sort(L, low, partition_index - 1)
            _quick_sort(L, partition_index + 1, high)

        _quick_sort(L, 0, len(L) - 1)
    return L


nums = [2,5,6,3,8,1]
print(quick_sort(nums))