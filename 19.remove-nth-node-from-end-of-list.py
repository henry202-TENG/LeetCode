#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        
        nth_node = head
        pointer = head

        for _ in range(n):
            pointer = pointer.next
            
        while True:
            # Ket point. 如果 n 是鏈錶的頭，pointer超出鍊錶的時候，去頭
            if not pointer:
                return head.next

            if pointer.next:
                pointer = pointer.next
                nth_node = nth_node.next
            else:
                nth_node.next = nth_node.next.next
                return head
        
# @lc code=end

