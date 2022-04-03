#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sym = 1
        digit_start = False
        digit = {"0":0, "1":1, "2":2, "3":3, "4":4, 
                 "5":5, "6":6, "7":7, "8":8, "9":9}

        for i, char in enumerate(s):
            if char in digit:
                digit_start = True
                if s[i-1] == "-" and i > 0:
                    sym = -1
                res *= 10
                res += int(char)
            elif not digit_start and char == " ":
                continue
            elif not digit_start and (char == "-" or char == "+"):
                if s[i-1] == " " or i == 0:
                    digit_start = True
                    continue
                else:
                    return 0
            elif not digit_start and char not in digit:
                return 0
            else:
                break

        if sym*res > pow(2, 31) - 1:
            res = pow(2, 31) - 1
        elif sym*res < -pow(2, 31):
            res = pow(2, 31)

        return sym*res
            

# @lc code=end

