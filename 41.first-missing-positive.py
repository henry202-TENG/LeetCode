#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1

        for i in range(len(nums)):
            nums[i] = nums[i] - 1

        res = min(res, min(nums))

        return res
        
# @lc code=end

