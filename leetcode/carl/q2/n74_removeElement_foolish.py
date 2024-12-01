# 双循环暴力方法解决

# 看代码随想录后自行编写

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            print(nums)
            if nums[i] == val:
                length -= 1
                for j in range(i, length, 1):
                    nums[j] = nums[j+1]
                i -= 1
            i += 1
        print(nums)
        return length
    
solution = Solution()
print(solution.removeElement([3,2,2,3], 3))
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))