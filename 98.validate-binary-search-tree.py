#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inner(root, MIN, MAX):
            if root:
                if MIN >= root.val or root.val >= MAX:
                    return False
                return  inner(root.left, MIN, root.val) and inner(root.right, root.val, MAX)

            return True

        return inner(root, -pow(2,32), pow(2,32))


        
# @lc code=end
