#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
        self.inorder = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inner(root):
            if root:
                inner(root.left)
                self.inorder.append(root.val)
                inner(root.right)

        inner(root)

        return self.inorder

        

        
# @lc code=end

