#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from re import search


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 雙binary
        # 模板二 + 模板一
        left = 0
        right = len(matrix)
        search_row = 0

        while left < right:
            mid = left + (right -left)//2
            if len(matrix) <= 1:
                break
            if target > matrix[-1][0]:
                search_row = len(matrix) -1
                break
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target < matrix[mid+1][0]:
                search_row = mid
                break
            if target > matrix[mid][0] :
                left = mid
            else:
                right = mid

        nums2 = matrix[search_row]
        left = 0
        right = len(nums2) - 1
        while left <= right:
            mid = left + (right -left)//2
            if nums2[mid] == target:
                return True
            if target > nums2[mid] :
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        

        
# @lc code=end

