/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        int x1 = reverse(x);
        return x1==x ? true : false;
    }

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

