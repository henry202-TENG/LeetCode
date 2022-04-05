#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""

        for s in address:
            if s == ".":
                res += "[.]"
            else:
                res += s

        return res
        
# @lc code=end

