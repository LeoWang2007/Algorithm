# 相向双指针方法

# 看代码随想录后自行编写

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        a = [int(0)] * len(nums)
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                a[i] = nums[l] ** 2
                l += 1
            else:
                a[i] = nums[r] ** 2
                r -= 1
            i -= 1
        return a
