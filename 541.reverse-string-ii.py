#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            b = a[i:i+k]
            a[i:i+k] = b[::-1]
        return "".join(a)
        
# @lc code=end

