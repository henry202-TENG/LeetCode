/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int count = 0;
        for (int i=0; i<n; i++)
        {
            if (nums[i] == val){
                swap(nums[i],nums[n-1-count]);
                count++;
                i--;
            }
            if (i == n-1-count)
            {
                break;
            }
        }
        return n-count;
    }
};
// @lc code=end

