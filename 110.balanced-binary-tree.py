#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getTreeDeep(self, root):
        if root:
            return 1+max(self.getTreeDeep(root.left), self.getTreeDeep(root.right))
        return 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            left_deep = self.getTreeDeep(root.left)
            right_deep = self.getTreeDeep(root.right)
            return abs(left_deep - right_deep) < 2 and \
                   self.isBalanced(root.right) and \
                   self.isBalanced(root.left)
        return True

        
# @lc code=end

