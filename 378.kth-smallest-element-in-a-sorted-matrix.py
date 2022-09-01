#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        jump_to = (k-1)//n
        posi_is = (k-1)%n

        return matrix[jump_to][posi_is]
        
# @lc code=end

