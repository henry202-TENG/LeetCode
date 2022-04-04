#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # x is the steps needed to cross the gap.
        x = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < x:
                x += 1
            else:
                x = 1
        return x == 1
                
        
# @lc code=end

