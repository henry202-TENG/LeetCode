#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        n = len(nums)
        if n == 0: return []

        head_p, tail_p = 0, 0
        res = []
        for i in range(1, n+1):

            if i == n or nums[i-1] + 1 != nums[i]:
                if head_p == tail_p:
                    temp = "{}".format(nums[head_p])
                else:
                    temp = "{}->{}".format(nums[head_p], nums[tail_p])
                head_p, tail_p = i, i
                res.append(temp)
                
                if i == n: continue

            if nums[i-1] + 1 == nums[i]:
                tail_p = i
                
        return res
        
# @lc code=end

