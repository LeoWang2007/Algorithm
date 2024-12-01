# 方法作废

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         LENGTH = len(nums)
#         current = (LENGTH - 1) // 2
#         for i in range(LENGTH // 2):
#             print(current)
#             CURRENT_NUM = nums[current]
#             if CURRENT_NUM == target:
#                 return current
#             elif CURRENT_NUM > target:
#                 current = current // 2
#             else:
#                 current += current // 2
#         return -1



solution = Solution()
print(solution.search([-1,0,3,5,6,7,8,9,12], 4))
# print(solution.search([-1,0,3,5,9,12], 2))
# print(solution.search([-1,0,3,5,9,12], 13))