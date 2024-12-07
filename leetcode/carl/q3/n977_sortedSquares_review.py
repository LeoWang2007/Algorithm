from typing import List


# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         l, r, cnt = 0, len(nums) - 1, len(nums) - 1
#         ans = [int(0)] * len(nums)
#         while l <= r:
#             if nums[l] ** 2 > nums[r] ** 2:
#                 ans[cnt] = nums[l] ** 2
#                 l += 1
#             else:
#                 ans[cnt] = nums[r] ** 2
#                 r -= 1
#             cnt -= 1
#         return ans

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, c = 0, len(nums) - 1, len(nums) - 1
        a = [int(0)] * len(nums)
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                a[c] = nums[l] ** 2
                l += 1
            else:
                a[c] = nums[r] ** 2
                r -= 1
            c -= 1
        return a