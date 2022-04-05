#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        count = 1
        m = len(matrix)
        n = len(matrix[0])
        m_top = 0
        m_bottom = m - 1
        n_left = 0
        n_right = n - 1

        while len(ans) < m*n:
            # 往右
            for i in range(n_right - n_left + 1):
                if len(ans) == m*n:
                    break
                ans.append(matrix[m_top][n_left + i])
            # 往下
            for i in range(m_bottom - m_top):
                if len(ans) == m*n:
                    break
                ans.append(matrix[m_top + i + 1][n_right])
            # 往左
            for i in range(n_right - n_left):
                if len(ans) == m*n:
                    break
                ans.append(matrix[m_bottom][n_right - i -1])
            # 往上
            for i in range(m_bottom - m_top - 1):
                if len(ans) == m*n:
                    break
                ans.append(matrix[m_bottom - i - 1][n_left])
            m_top += 1
            m_bottom -= 1
            n_left += 1
            n_right -= 1
        return ans
        
# @lc code=end

