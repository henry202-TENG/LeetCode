#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        mask = list(range(numRows)) + list(reversed(range(1, numRows-1)))
        mask_len = len(mask)
        res = ""
        hash = {}

        for i in range(numRows):
            hash[i] = ""
            
        for index, x in enumerate(s):
            hash[mask[index%mask_len]] += x

        for i in range(numRows):
            res += hash[i]


        return res
 
# @lc code=end
