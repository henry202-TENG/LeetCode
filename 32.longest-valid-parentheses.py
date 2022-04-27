#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def vaildParentheses(self, sub_s):
        count, left, right = 0, 0, 0
        for s in sub_s:
            if s == "(":
                left += 1
            if s == ")":
                right +=1
                if right > left:
                    break
            if left == right:
                count = left

        return 2*count, right

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        Max = 0
        index = 0

        while index < n:
            sub_s = s[index:]
            temp_max, right = self.vaildParentheses(sub_s)
            if temp_max > Max:
                Max = temp_max
            index += temp_max + 1

            if right == 0:
                break

        return Max
        
# @lc code=end

