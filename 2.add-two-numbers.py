#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        digit_to_add = 0


        while l1 or l2:
            curr.next = ListNode()
            curr = curr.next

            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            temp += digit_to_add
            curr.val = temp%10
            digit_to_add = temp//10

        # Key point. Remember to process final digit
        if digit_to_add:
            curr.next = ListNode(digit_to_add)

        # Key point. Why return res.next.
        return res.next

        
# @lc code=end

