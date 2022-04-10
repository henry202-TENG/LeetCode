#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        set_K = set(nums)
        hash = {}
        while set_K:
            hash[set_K.pop()] = 0

        for ele in nums:
            hash[ele] += 1
            if hash[ele] > n/2:
                return ele

# @lc code=end

