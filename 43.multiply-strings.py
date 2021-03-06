#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # The ord() function returns an integer representing the Unicode character.
        # The chr() method returns a character (a string) from an integer 
        def str2int(input):
            int1 = 0
            for s in input:
                int1 *= 10
                int1 += ord(s)-ord("0")
            return int1

        def int2str(input):
            if input == 0: return "0"
            s = ""
            while input:
                s = chr(input%10 + ord("0")) + s
                input //= 10
            return s

        return int2str(str2int(num1)*str2int(num2))
        
# @lc code=end

