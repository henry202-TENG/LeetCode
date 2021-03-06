/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        int mid;
        while (left <= right)
        {
            mid = left + (right - left)/2;
            if (nums[mid] == target) return mid;

            if (nums[mid] < target) left = mid+1;
            else right = mid-1;
        }
        if (nums[mid] < target)
        {
            return mid+1;
        }
        else
        {
            return mid;
        }
    }
};
// @lc code=end

