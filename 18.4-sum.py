#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        p1 = 0
        p2 = 1
        p3 = 3
        p4 = len(nums) - 1

        res = []

        while p1+2 < len(nums) - 1:

            while p3 < p4:
                sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                if sum == target:
                    res.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                if sum > target:
                    p3 -= 1
                else:
                    p4 += 1

            if p2+1 < p3:
                p2 += 1
                p1, p2, p3, p4 = p1, p2, p2+1, len(nums) - 1
            else:
                p1 += 1
                p1, p2, p3, p4 = p1, p1+1, p1+2, len(nums) - 1


        res_f = []
        [res_f.append(x) for x in res if x not in res_f]
        return res_f
        
# @lc code=end

