#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def inner(a, l, r):
            if l==r:
                res.append(a[:])
            else:
                for i in range(l,r+1):
                    a[l], a[i] = a[i], a[l]
                    inner(a, l+1, r)
                    a[i], a[l] = a[l], a[i] # backtrack

        n = len(nums)
        res = []
        inner(nums, 0, n-1)

        return res
 
# @lc code=end

