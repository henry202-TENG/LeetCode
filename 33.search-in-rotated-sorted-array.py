#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 判斷有沒有錯序
        # 找出分界
        # 在其中一部分再尋找

        # 判斷有沒有錯序
        search_divider = False
        if nums[0] > nums[-1]:
            search_divider = True

        left = 0
        right = len(nums) - 1
        divider = 0
        # 找出分界
        while left <= right and search_divider:
            mid = left + (right - left)//2
            if nums[mid-1] < nums[mid] and  nums[mid] > nums[mid+1]:
                divider = mid
                break
            if  nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        # 判斷要前半部還是後半部
        if target >= nums[0] and search_divider:
            left = 0
            right = divider
        elif target < nums[0] and search_divider:
            left = divider + 1
            right = len(nums) - 1

        if not search_divider:
            left = 0
            right = len(nums) - 1

        # 在其中一半部尋找
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
# @lc code=end

