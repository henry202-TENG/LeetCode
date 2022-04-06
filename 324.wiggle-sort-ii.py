#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 從最大的開始依次放在偶位
        # 偶位放完放奇位
        # 從大的開始依次放在奇位
        n = len(nums)
        in_sort = sorted(nums)
        
        idx = n -1

        for i in range(1, n, 2):
            nums[i] = in_sort[idx]
            idx-=1

        for i in range(0, n, 2):
            nums[i] = in_sort[idx]
            idx-=1



        
# @lc code=end

