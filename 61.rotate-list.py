#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get list node 長度
        # rotate = k % list_len
        # 第一個指針先走 rotate 距離
        # 第二指針開始，直到第一指針走到尾
        # 第二指針所在位置是新的尾
        # 新的head 是第二指針下一個
        # 令新的尾指向 None
        # 第一指針指導新舊的頭連接

        # Get list node 長度
        list_len = 0
        curr = head
        while curr:
            curr = curr.next
            list_len += 1
        # key point
        if list_len == 0: return head

        # rotate = k % list_len
        First_p = head
        curr = head
        rotate = k%list_len
        # key point
        if rotate == 0: return head

        # 第一個指針先走 rotate 距離
        for _ in range(rotate):
            First_p = First_p.next

        # 第二指針開始，直到第一指針走到尾
        while First_p.next:
            First_p = First_p.next
            curr = curr.next

        # 重新連接
        new_head = curr.next
        curr.next = None
        First_p.next = head

        return new_head

# @lc code=end

