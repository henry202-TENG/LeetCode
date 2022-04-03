#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 
                 400:"CD", 500:"D", 900:"CM", 1000:"M"}

        roman_d = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ""
        while num:
            for divider in roman_d:
                yes = num // divider
                remain = num % divider
                num = remain

                if yes:
                    res += roman[divider]*yes

        return res

# @lc code=end

