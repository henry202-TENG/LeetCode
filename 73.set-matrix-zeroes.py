#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # remember i, j which are going to set 0.
        # set 0 according to hash table
        hash_i = {}
        hash_j = {}
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    hash_i[i] = 0
                    hash_j[j] = 0

        for i in range(m):
            if i in hash_i:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if j in hash_j:
                for i in range(m):
                    matrix[i][j] = 0
        
        
# @lc code=end

