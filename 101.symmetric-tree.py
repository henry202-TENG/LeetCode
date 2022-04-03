#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BFS(self, root_l, root_r):
        if root_l == None and root_r == None: return True
        if root_l != None and root_r == None: return False
        if root_l == None and root_r != None: return False

        if root_l.val != root_r.val: return False

        res1 = self.BFS(root_l.left, root_r.right)
        res2 = self.BFS(root_l.right, root_r.left)

        return res1 and res2

    def DFS(self, root_l, root_r):
        pass



    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.BFS(root.left, root.right)
        
# @lc code=end

