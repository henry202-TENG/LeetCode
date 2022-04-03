#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.inOrder = []

    def inOrderTraseval(self, root):
        if root:
            self.inOrderTraseval(root.left)
            self.inOrder.append(root.val)
            self.inOrderTraseval(root.right)

    def inOrderAssign(self, root):
        if root:
            self.inOrderAssign(root.left)
            root.val = self.inOrder.pop(0)
            self.inOrderAssign(root.right)


    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inOrderTraseval(root)
        self.inOrder.sort()
        self.inOrderAssign(root)


        
# @lc code=end

