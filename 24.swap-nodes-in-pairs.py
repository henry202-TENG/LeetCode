#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or not head.next: return head
        new_head = head.next
        pointer0 = None
        pointer1 = head
        pointer2 = head.next

        while True:
            pointer1.next = pointer2.next
            pointer2.next = pointer1
            pointer0 = pointer1

            pointer1 = pointer1.next
            if not pointer1:
                break
            pointer2 = pointer1.next
            if not pointer2:
                break
            
            pointer0.next = pointer2

        
        
        return new_head


# @lc code=end

