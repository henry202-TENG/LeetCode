#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [i+1 for i in range(n)]
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
        
# @lc code=end

