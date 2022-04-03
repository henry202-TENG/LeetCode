#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from copy import copy


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp=[[1 for _ in range(n)]for _ in range(m)]

        zero_flag = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                zero_flag = True
            if zero_flag:
                dp[i][0] = 0

        zero_flag = False
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                zero_flag = True
            if zero_flag:
                dp[0][i] = 0

        for i in range(1, m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


        
# @lc code=end

