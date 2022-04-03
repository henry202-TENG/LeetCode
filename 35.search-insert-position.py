#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #模板2
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right -left)//2
            if nums[mid-1] < target <= nums[mid] :
                return  mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return None

        
# @lc code=end

