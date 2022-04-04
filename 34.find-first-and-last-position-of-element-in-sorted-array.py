#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        一個想法:BS找到目標後, 將目標左右子陣列在尋找一次, 如果有找到,則更新左右邊界
        '''
        # 找到目標
        # 以目標為中心擴散
        left = 0
        right = len(nums) - 1
        center = -1
        range = [-1, -1]

        # 找到目標
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                center = mid
                range = [mid, mid]
                break
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1

        # 以目標為中心擴散
        if center != -1:
            index = 1
            right_end = False
            left_end = False
            while True:
                if mid - index >=0 and nums[mid - index] == target:
                    range[0] = mid - index
                else:
                    left_end = True
                if mid + index <= len(nums) - 1 and nums[mid + index] == target:
                    range[1] = mid + index
                else:
                    right_end = True
                
                if left_end and right_end:
                    break
                index += 1

        return range


        
# @lc code=end

