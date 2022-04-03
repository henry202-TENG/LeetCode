#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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

    def zigzag(self, level, root):
        if level % 2:
            self.res[level].append(root.val)
        else:
            self.res[level].insert(0, root.val)

    def BFS(self, level, root):
        if level > len(self.res)-1 and (root.left != None or root.right != None): self.res.append([])
        
        if root.right != None:
            self.zigzag(level, root.right)
            self.BFS(level+1, root.right)
        
        if root.left != None:
            self.zigzag(level, root.left)
            self.BFS(level+1, root.left)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return self.res
        level = 1
        self.res = [[root.val]]

        self.BFS(level, root)

        return self.res
        
# @lc code=end

