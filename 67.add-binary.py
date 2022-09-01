#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def binToInt(self, a:str)->int:
        index = 1
        ans = 0
        for i in range(len(a)):
            ans += int(a[len(a)-i-1])*index
            index *= 2
        return ans

    def intTobin(self, c:int)->str:
        ans = bin(c)
        return ans[2:]

    def addBinary(self, a: str, b: str) -> str:
        int_a, int_b = self.binToInt(a), self.binToInt(b)
        return self.intTobin(int_a + int_b)

        
# @lc code=end

