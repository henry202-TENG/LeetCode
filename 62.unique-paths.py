#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        matrix = [[1]*n]*m

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]

        """
        def goTo2(i, j):
            if i == 0 and j == 0: return 1

            if i == 0 and j > 0:
                return goTo2(i, j-1)
            if i > 0 and j == 0:
                return goTo2(i-1, j)

            if i > 0 and j > 0:
                return goTo2(i, j-1) + goTo2(i-1, j)


        return goTo2(m-1, n-1)
        """
        
# @lc code=end

