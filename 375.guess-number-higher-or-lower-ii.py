#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:

        # Problem:
        # Q1: What is the "worst"? 
        # For a step, whatever I make guess, thing tend to MAXIMUM the cost

        # Q2: What is the retriction of "worst"? How I guarantee? 
        # I choose the MINIMUM cost for each step.
        # 
        dp1 = [[0 for _ in range(n+1)] for _ in range(n+1)]

        def dynP(dp, i, j):
            if i >= j: return 0
            if dp[i][j] != 0: return dp[i][j]
            res = float('inf')
            for kk in range(i, j+1):
                temp = kk + max(dynP(dp, i, kk-1), dynP(dp, kk+1, j))
                res = min(temp, res)
            dp[i][j] = res
            return res
        
        return dynP(dp1, 1, n)
        
# @lc code=end

