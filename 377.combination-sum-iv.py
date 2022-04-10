#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # back teacking take too nuch time.
        nums.sort()
        def backtrack(nums, target, sum, count):
            for n in nums:
                if sum+n > target: break
                if sum+n == target:
                    count += 1
                else:
                    count = backtrack(nums, target, sum+n, count)
            return count
        return backtrack(nums, target, 0, 0)
        '''
        dp = [0]*(target + 1)
        dp[0] = 1
        nums.sort()

        for i in range(target + 1):
            for n in nums:
                if n > i: break
                if n == i: dp[i] += 1
                if n < i: dp[i] += dp[i-n]
        return dp[-1]
        '''

# @lc code=end

