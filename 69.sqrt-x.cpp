/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
public:
    int mySqrt(int x) {
        int left = 0;
        int right = __INT_MAX__;
        int mid;
        if (x == 0) return 0;

        while (left <= right)
        {
            mid = left + (right - left)/2;
            if (mid == x/mid || (mid < x/mid && x/(mid+1) < (mid+1))) return mid;
            if (mid < x/mid) left = mid+1;
            else right = mid-1;
        }
        return -1;

        /*
        long int y = 0;
        while (y*y<=x)
        {
            y++;
        }
        return y-1;
        */
    }
};
// @lc code=end

