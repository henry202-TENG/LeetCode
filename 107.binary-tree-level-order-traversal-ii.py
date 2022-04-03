#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
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
        self.res = []

    def BFS(self, level, root):
        if level > len(self.res)-1 and (root.left != None or root.right != None): self.res.append([])

        if root.left != None:
            self.res[level].append(root.left.val)
            self.BFS(level+1, root.left)

        if root.right != None:
            self.res[level].append(root.right.val)
            self.BFS(level+1, root.right)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return self.res
        level = 1
        self.res = [[root.val]]

        self.BFS(level, root)

        return reversed(self.res)
        
        
# @lc code=end

