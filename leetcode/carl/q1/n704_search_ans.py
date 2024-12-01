# 看代码随想录后自行编写

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            # 注意是加不是减
            current = (right + left) // 2
            if nums[current] > target:
                right = current - 1
            elif nums[current] < target:
                left = current + 1
            else:
                return current
        return -1

solution = Solution()
print(solution.search([-1,0,3,5,6,7,8,9,12], 4))
print("===")
print(solution.search([-1,0,3,5,9,12], 2))
print("===")
print(solution.search([-1,0,3,5,9,12], 9))
print("===")
print(solution.search([-1,0,3,5,9,12], 13))
print("===")
print(solution.search([-1,0,3,5,9,12], -2))