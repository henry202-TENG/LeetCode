#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
        self.MAXDeep = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        deep = 0

        def inner(root, deep):
            if root:
                deep += 1
                if deep > self.MAXDeep:
                    self.MAXDeep = deep
                inner(root.left, deep)
                inner(root.right, deep)
        
        inner(root, deep)

        return self.MAXDeep
        
# @lc code=end

