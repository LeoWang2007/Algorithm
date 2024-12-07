# 复习-自己重写左闭右开

from typing import List


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             mid = left + (right - 1 - left) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid
#             else:
#                 return mid
#         return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = l + (r - 1 - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
            else:
                return m
        return -1
