#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.maximum = 1
        self.res_arr = []

    def lengthOfLIS(self, nums: List[int]) -> int:

        def DP(arr):
            n = len(arr)
 
            # Declare the list (array) for LIS and
            # initialize LIS values for all indexes
            lis = [1]*n
        
            # Compute optimized LIS values in bottom up manner
            for i in range(1, n):
                for j in range(0, i):
                    if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                        lis[i] = lis[j]+1
        
            # Initialize maximum to 0 to get
            # the maximum of all LIS
            self.maximum = 0
        
            # Pick maximum of all LIS values
            for i in range(n):
                self.maximum = max(self.maximum, lis[i])
        
            return self.maximum

            

        DP(nums)
        return self.maximum
 
# @lc code=end

