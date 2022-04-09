#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
from operator import truediv


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False

        while n > 0:
            if abs(n) == 1: return True
            if n%3 != 0: return False
            n//=3

        return True
        
# @lc code=end

