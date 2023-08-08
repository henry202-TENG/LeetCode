#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, num in enumerate(nums):
            if target - num not in hash_table:
                hash_table[target - num] = index
            if num in hash_table and hash_table[num] != index:
                return [index, hash_table[num]]

# @lc code=end

