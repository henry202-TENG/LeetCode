#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def boxMapping(i, j):
            return i//3 + 3*(j//3)

        n = 9
        hash_row = []
        hash_col = []
        hash_box = []

        for i in range(n):
            hash_row.append({})
            hash_col.append({})
            hash_box.append({})

        for i in range(n):
            for j in range(n):
                target = board[i][j]
                if target != ".":
                    if target not in hash_row[i]:
                        hash_row[i][target] = 1
                    else:
                        return False

                    if target not in hash_col[j]:
                        hash_col[j][target] = 1
                    else:
                        return False

                    if target not in hash_box[boxMapping(i,j)]:
                        hash_box[boxMapping(i,j)][target] = 1
                    else:
                        return False
        return True

        
# @lc code=end

