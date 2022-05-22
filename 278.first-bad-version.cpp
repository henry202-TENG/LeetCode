/*
 * @lc app=leetcode id=278 lang=cpp
 *
 * [278] First Bad Version
 */

// @lc code=start
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        int mid;

        while (left <= right)
        {
            mid = left + (right -left)/2;
            if (isBadVersion(mid-1)^isBadVersion(mid)) return mid;

            if (isBadVersion(mid)) right = mid -1;
            else left = mid +1;
        }
        return -1;
    }
};
// @lc code=end

