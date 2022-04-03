#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack("", n, 0, 0)
        return self.res


    def backtrack(self, S, n, left, right):
        if n == right and left == right:
            self.res.append(S)
            return
        
        if left > right:
            self.backtrack(S+")", n, left, right+1)
        if left < n:
            self.backtrack(S+"(", n, left+1, right)
        
# @lc code=end

