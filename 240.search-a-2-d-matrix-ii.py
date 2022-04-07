#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return False

class Solution:
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if binary_search(i,0,len(i)-1,target):
                return True
        return False
    '''
    # 從右上角開始，如果比目標小，則往下走，如果比目標大，則往左走
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        def check(matrix, r,c):
            if c<0 or r>len(matrix)-1: return False
            if matrix[r][c] == target: return True
            if matrix[r][c] > target:
                return check(matrix,r,c-1)
            return check(matrix,r+1,c)
        
        return check(matrix, 0, len(matrix[0])-1)
         



# @lc code=end

