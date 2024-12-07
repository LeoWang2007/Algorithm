# 复习-自己重写

from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         slow = 0
#         for fast in range(len(nums)):
#             nums[slow] = nums[fast]
#             if nums[fast] != val:
#                 slow += 1
#         return slow

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0
        for f in range(len(nums)):
            nums[s] = nums[f]
            if nums[f] != val:
                s += 1
        return s