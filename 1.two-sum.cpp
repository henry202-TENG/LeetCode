/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        for (vector<int>::size_type i = 0; i!=nums.size()-1; i++)
        {
            for (vector<int>::size_type j = i+1; j!=nums.size(); j++)
            {
                if (nums[i]+nums[j] == target)
                {
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        }


        return res;
    }
};
// @lc code=end

