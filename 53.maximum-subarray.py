#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def MaxSubarray(arr):
            if len(arr) == 1: return nums[0]
            maximum = arr[0]
            lis = arr
            for i in range(1, len(arr)):
                if arr[i-1] > 0:
                    lis[i] += arr[i-1]
                if lis[i] > maximum:
                    maximum = lis[i]
            return maximum
            
        return MaxSubarray(nums)

        
# @lc code=end

