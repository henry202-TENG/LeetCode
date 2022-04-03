#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = 0

    def backtracking(self, n, node, step2):
        if n == node and step2:
            self.res += 2
            return
        elif n == node and not step2:
            self.res += 1
            return

        if node + 1 <= n and node == 0:
            self.backtracking(n, node+1, False)

        if node + 1 <= n and node != 0:
            self.backtracking(n, node+1, False)
            self.backtracking(n, node+1, False)

        if node + 2 <= n and node != 0:
            self.backtracking(n, node+2, True)



    def numTrees(self, n: int) -> int:

        self.backtracking(n, 0, False)

        return self.res
        
# @lc code=end

