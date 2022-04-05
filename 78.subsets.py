#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.recur(nums, 0, [])
        return self.ret
            
    def recur(self, nums: List[int], pos: int, tmp_ret: List[int]) -> None:
        # base condition:
        if pos == len(nums):
            self.ret.append(tmp_ret)
            return
        
        # condition 1: use the current element
        tmp_ret.append(nums[pos])
        self.recur(nums, pos+1, tmp_ret[:])
        tmp_ret.pop()
        
        # condition 2: do not use the current element
        self.recur(nums, pos+1, tmp_ret[:])
# @lc code=end

