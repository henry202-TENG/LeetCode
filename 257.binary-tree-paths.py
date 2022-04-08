#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def inorder(root, temp):
            if root:
                temp.append(root.val)
                inorder(root.left, temp)
                if not root.left and not root.right:
                    res.append(temp[:])
                inorder(root.right, temp)
                temp.pop()

        def toStr(arr):
            res = ""
            for n in arr:
                if len(res) == 0:
                    res += str(n)
                else:
                    res += "->{}".format(n)
            return res
        
        inorder(root, [])
        res2 = []

        for arr in res:
            res2.append(toStr(arr))

        return res2
        
# @lc code=end

