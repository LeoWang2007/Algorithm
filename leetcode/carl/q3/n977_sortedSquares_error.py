# 临时存储法-自行实现方法

# 未通过所有测试

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = 0
        ans = []
        temp = []
        flag = False
        for item in nums:
            res = item*item
            if item >= 0 and not flag:
                flag = True
            if flag:
                if temp:
                    while temp[len(temp) - cnt - 1] <= res:
                        ans.append(temp[len(temp) - cnt - 1])
                        cnt += 1
                        if cnt >= len(temp):
                            break
                ans.append(res)
            else:
                temp.append(res)
            print(ans)
        if cnt < len(temp):
            for item in temp[-1::-1]:
                ans.append(item)
        return ans
