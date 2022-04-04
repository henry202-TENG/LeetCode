#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the largest k, where nums[k] < nums[k+1]
        # Find the largest l, where l>k and nums[k] < nums[l]
        # Swap nums[k] and nums[l].
        # Reverse the sub-array nums[k + 1:].
        k = len(nums) - 1
        while k > 0 and nums[k-1] >= nums[k]: k -= 1

        if k == 0: 
            nums[:] = nums[::-1]
            return

        # key point. 
        k -= 1

        l = len(nums) - 1
        while nums[l] <= nums[k] and k < l: l -= 1

        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[k+1:][::-1] 


        
# @lc code=end

