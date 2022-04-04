#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False

        temp1 = str(x)
        temp2 = ""
        for i in range(len(temp1)):
            temp2 += temp1[len(temp1)-1-i]

        return int(temp2) == x
        
# @lc code=end

