#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        point1 = 0
        point2 = len(height) - 1

        while point1 < point2:
            area = min(height[point1], height[point2]) * (point2-point1)

            if area > max:
                max = area
            
            if height[point1] > height[point2]:
                point2 -= 1
            else:
                point1 += 1
            
        return max

# @lc code=end

