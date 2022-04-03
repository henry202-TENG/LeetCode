#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        index = 0
        while index < len(nums):
            Max = 0
            Max_index = 0
            for i in range(1, index+2):
                if Max < nums[index + i]:
                    Max_index = index + i

            index = index + nums[Max_index]

            if index >= len(nums) - 1:
                return True

        return False
                
        
# @lc code=end

