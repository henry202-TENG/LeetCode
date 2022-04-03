#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        res = 0
        
        if (dividend<0 and divisor<0) or (dividend>=0 and divisor>=0) :
            sym = 1
        else:
            sym = -1

        while dividend_abs >= divisor_abs:
            count = 0
            while True:
                if dividend_abs >= divisor_abs << count:
                    count += 1
                else:
                    count -= 1
                    dividend_abs -= (divisor_abs<<count)
                    res += 1<<count
                    break

        if sym*res > pow(2,31) - 1:
            res = pow(2,31) - 1
        elif sym*res < -pow(2,31):
            res = pow(2,31)


        return sym*res

# @lc code=end

