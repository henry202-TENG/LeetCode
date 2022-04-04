#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] not in hash:
                hash[target - nums[i]] = i
            if nums[i] in hash and hash[nums[i]] != i:
                return [i, hash[nums[i]]]
        
# @lc code=end

