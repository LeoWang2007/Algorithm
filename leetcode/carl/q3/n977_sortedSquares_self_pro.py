# 临时存储法-自行实现方法

# cnt相比于前一版本采用逆序，减少运算

# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         i = 0
#         cnt = 0
#         ans = []
#         temp = []
#         while i < len(nums):
#             if nums[i] >= 0:
#                 break
#             temp.append(nums[i]*nums[i])
#             i += 1
#         cnt = len(temp) - 1
#         while i < len(nums):
#             while cnt >= 0:
#                 if temp[cnt] > nums[i]*nums[i]:
#                     break
#                 ans.append(temp[cnt])
#                 cnt -= 1
#             ans.append(nums[i]*nums[i])
#             i += 1
#         for i in range(cnt, -1, -1):
#             ans.append(temp[i])
#         return ans

# # 使用临时变量存储
# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         i = 0
#         n = 0
#         a = []
#         t = []
#         while i < len(nums):
#             if nums[i] >= 0:
#                 break
#             t.append(nums[i]*nums[i])
#             i += 1
#         n = len(t) - 1
#         while i < len(nums):
#             while n >= 0:
#                 if t[n] > nums[i]*nums[i]:
#                     break
#                 a.append(t[n])
#                 n -= 1
#             a.append(nums[i]*nums[i])
#             i += 1
#         for i in range(n, -1, -1):
#             a.append(t[i])
#         return a

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:  
        i = 0
        n = 0
        a = []
        while i < len(nums):
            if nums[i] >= 0:
                break
            nums[n] = nums[i]*nums[i]
            n += 1
            i += 1
        n -= 1
        while i < len(nums):
            while n >= 0:
                if nums[n] > nums[i]*nums[i]:
                    break
                a.append(nums[n])
                n -= 1
            a.append(nums[i]*nums[i])
            i += 1
        for i in range(n, -1, -1):
            a.append(nums[i])
        return a