'''
全探索（リニアサーチ）
'''

from typing import List, NewType

IndexNum = NewType('IndexNum', int)


def linear_search(L: List[int], value: int) -> IndexNum:
    for i in range(len(L)):
        if L[i] == value:
            return i
    return -1


nums = [2,5,6,3,8,1]
print(linear_search(nums, 1))

# 5回