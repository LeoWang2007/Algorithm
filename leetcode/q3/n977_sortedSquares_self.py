# 临时存储法-自行实现方法

# 通过 25ms

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        cnt = 0
        ans = []
        temp = []
        while i < len(nums):
            if nums[i] >= 0:
                break
            temp.append(nums[i]*nums[i])
            i += 1
        while i < len(nums):
            while cnt < len(temp):
                if temp[len(temp) - cnt - 1] > nums[i]*nums[i]:
                    break
                ans.append(temp[len(temp) - cnt - 1])
                cnt += 1
            ans.append(nums[i]*nums[i])
            i += 1
        for i in range(cnt, len(temp)):
            ans.append(temp[len(temp) - i - 1])
        return ans
