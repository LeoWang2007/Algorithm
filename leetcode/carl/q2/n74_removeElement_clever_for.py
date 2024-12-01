# 双指针解法使用for循环

# 看代码随想录后自行编写
# 一开始记错了，以为这个方法也需要中途修改指针，所以使用了while

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
    
solution = Solution()
print(solution.removeElement([3,2,2,3], 3))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))