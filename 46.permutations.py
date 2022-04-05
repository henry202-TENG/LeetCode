#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # The idea is that 1st ele can swap with ele after 1st ele.
        # 2ed ele can swap with ele after 2ed ele.
        # .
        # .
        # .

        # l is the position we at.
        def trackBack(a, l):
            # l is at the end of nums then append.
            if l==n-1:
                res.append(a[:])
            else:
                # swap with the following element.
                for i in range(l,n):
                    a[l], a[i] = a[i], a[l]
                    trackBack(a, l+1)
                    a[i], a[l] = a[l], a[i] # backtrack

        n = len(nums)
        res = []
        trackBack(nums, 0)

        return res
 
# @lc code=end

