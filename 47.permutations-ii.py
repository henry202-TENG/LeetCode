#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)

        def dfs(curr):
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in range(k):
                res.append(nums[i])
                dfs(res)
                res.pop()

        res = []
        dfs([])

        return res
        


        
# @lc code=end

