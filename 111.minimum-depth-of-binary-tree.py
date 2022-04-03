#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
        self.min_d = -1

    def DFS(self, root, depth):
        if self.min_d != -1 and depth > self.min_d: return
        if root.left == None and root.right == None:
            if self.min_d == -1:
                self.min_d = depth
            elif depth < self.min_d:
                self.min_d = depth

        if root.left != None:
            self.DFS(root.left, depth+1)
        if root.right != None:
            self.DFS(root.right, depth+1)

    def BFS(self, root, depth):
        if root == None: return
        q = [root]
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if self.min_d != -1 and depth > self.min_d: return
                if node.left == None and node.right == None:
                    if self.min_d == -1:
                        self.min_d = depth
                    elif depth < self.min_d:
                        self.min_d = depth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        self.BFS(root, 1)
        self.DFS(root, 1)

        return self.min_d


        
# @lc code=end

