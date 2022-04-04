#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # for index, choose the step that go as far as it can.
        if len(nums) ==1: return 0
        count = 0
        index = 0
        while index <= len(nums)-1:
            temp_max_jump = 0
            choose_step = 0
            for i in range(nums[index] + 1):
                # choose step
                if index + i >= len(nums)-1:
                    return count+1
                if nums[index + i] + i > temp_max_jump:
                    temp_max_jump = nums[index + i] + i
                    choose_step = i
            count+=1
            
            if index + i >= len(nums)-1:
                break
            else:
                index += choose_step
            
        return count
        
# @lc code=end

