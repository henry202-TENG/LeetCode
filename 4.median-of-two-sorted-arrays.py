#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        len1 = len(nums1)
        len2 = len(nums2)
        i,j = 0, 0
        min_l = 0
        min_r = 0

        while i+j < (len1+len2)//2+1:
            if i != len1 and j != len2:
                if nums1[i] > nums2[j]:
                    min_l = min_r
                    min_r = nums2[j]
                    j+=1
                else:
                    min_l = min_r
                    min_r = nums1[i]
                    i+=1
            elif i != len1:
                min_l = min_r
                min_r = nums1[i]
                i+=1
            elif j != len2:
                min_l = min_r
                min_r = nums2[j]
                j+=1

        return min_r if (len1+len2)%2==1 else (min_l+min_r)/2
        '''
        len1 = len(nums1)
        len2 = len(nums2)
        left_1 = 0
        left_2 = 0
        right_1 = len1 - 1
        right_2 = len2 - 1
        val_1 = 0
        val_2 = 0

        while (mid_1 + mid_2) < (len1 + len2)//2 - 1:
            mid_1 = (left_1 + right_1) // 2
            mid_2 = (left_2 + right_2) // 2

            if mid_1 < mid_2:
                left_1 = mid_1
                right_2 = mid_2
                val_1 = nums1[mid_1]
                val_2 = nums2[mid_2]
            else:
                left_2 = mid_2
                right_1 = mid_1
                val_1 = nums1[mid_1]
                val_2 = nums2[mid_2]
            print(mid_1)
            print(mid_2)

        return val_1 if (len1 + len2)%2==0 else (val_1 + val_2)/2

# @lc code=end

