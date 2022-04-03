#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sym = 1

        if x < 0:
            x = -x
            sym = -1

        while x:
            res *= 10
            res += x%10
            x //= 10

        res *= sym

        if res > pow(2,31) - 1 or res < -pow(2,31): return 0
        
        return res
        
# @lc code=end

