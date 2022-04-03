#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def _innerLIS(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l-=1; r+=1
            return s[l+1 : r]


        def LIS(s):
            if len(s) <= 1 : return s
            longest_res = ""
            temp_res = ""
            
            for i in range(len(s)):
                temp_res = _innerLIS(s, i, i)
                if len(temp_res) > len(longest_res):
                    longest_res = temp_res

                temp_res = _innerLIS(s, i, i+1)
                if len(temp_res) > len(longest_res):
                    longest_res = temp_res

            return longest_res

        return LIS(s)
        
# @lc code=end

