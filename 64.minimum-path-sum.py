#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = grid.copy()

        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        for i in range(1, n):
            dp[0][i] += dp[0][i-1]

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j-1] < dp[i-1][j]:
                    dp[i][j] += dp[i][j-1]
                else:
                    dp[i][j] += dp[i-1][j]

        return dp[m-1][n-1]


        
# @lc code=end

