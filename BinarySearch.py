'''
バイナリーサーチ
'''

from typing import List, NewType

IndexNum = NewType('IndexNum', int)


def binary_search(L: List[int], value: int) -> IndexNum:
    left, right = 0, len(L)-1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == value:
            return mid
        elif L[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int, left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            return _binary_search(numbers, value, left, mid - 1)
    return _binary_search(numbers, value, 0, len(numbers) - 1)


nums = [1,2,5,7,10,13]
print(binary_search(nums, 10))

# 5回