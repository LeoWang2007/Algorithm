# 方法作废

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        LENGTH = len(nums)
        last = -2
        current = (LENGTH - 1) // 2
        print(current)
        while current >= 0 and current < LENGTH:
            CURRENT_NUM = nums[current]
            if CURRENT_NUM == target:
                return current
            else:
                if abs(current - last) == 1:
                    print(111)
                    return -1
                last = current
                if CURRENT_NUM > target:
                    current = current // 2
                else:
                    current += current // 2
            print(current)
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