#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while len(ans) < m*n:
            # 往右
            for i in range(right - left + 1):
                if len(ans) == m*n:
                    break
                ans.append(matrix[top][left + i])
            # 往下
            for i in range(bottom - top):
                if len(ans) == m*n:
                    break
                ans.append(matrix[top + i + 1][right])
            # 往左
            for i in range(right - left):
                if len(ans) == m*n:
                    break
                ans.append(matrix[bottom][right - i -1])
            # 往上
            for i in range(bottom - top - 1):
                if len(ans) == m*n:
                    break
                ans.append(matrix[bottom - i - 1][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans
        
# @lc code=end

