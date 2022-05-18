/*
 * @lc app=leetcode id=7 lang=cpp
 *
 * [7] Reverse Integer
 */

// @lc code=start
class Solution {
public:
    int reverse(int x) {
        long int res = 0;
        long int sign = x >= 0 ? 1 : -1;
        long int xx = sign*x;
        while (xx)
        {
            long int temp = xx%10;
            xx /= 10;
            res *= 10;
            res += temp;
        }
        res *= sign;
        if (res > INT_MAX || res < INT_MIN) return 0;
        return res;
    }
};
// @lc code=end

