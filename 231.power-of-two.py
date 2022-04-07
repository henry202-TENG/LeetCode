#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0: return False

        while n:
            if n != 1 and n % 2 != 0: return False
            n >>= 1

        return True

        
# @lc code=end

