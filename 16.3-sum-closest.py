#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from ctypes import pointer


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # two pointer and search rest of array
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        index1, index2, index3 = 0, 1, len(nums)-1

        while index1 < len(nums) - 2:
            index2, index3 = index1+1, len(nums)-1
            while index2 < index3:
                sum = nums[index1]+nums[index2]+nums[index3]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(res - target):
                    res = sum

                if sum > target:
                    index3 -= 1
                else:
                    index2 += 1
            index1 += 1
        return res
                    

        
# @lc code=end

