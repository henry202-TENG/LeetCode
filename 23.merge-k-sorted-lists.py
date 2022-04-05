#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 如果list為空，則返回空
        # 取得鏈表中最小值
        # 對每個鍊錶，如果head.val==point_val，則取走接到新鍊錶，直到遇到比point_val大，則換下一個
        # 使用 queue的方式處理鍊錶

        if len(lists) == 0: return None

        point_val = 1000000
        for listNode in lists:
            if listNode and listNode.val < point_val:
                point_val = listNode.val

        res = ListNode()
        curr = res
        while lists:
            n = len(lists)
            for _ in range(n):
                listNode = lists.pop(0)
                if listNode:
                    new_listNode = listNode
                    while listNode and listNode.val == point_val:
                        new_listNode = listNode.next # 鍊錶被取走頭之後的新頭
                        curr.next = listNode         # 被取走的node接到答案後面
                        listNode.next = None         # 答案最後node指向 None
                        curr = curr.next             # 從新標定答案鏈尾
                        listNode = new_listNode      # listNode 指向新錶頭，為了進行下一個循環
                    if new_listNode:
                        lists.append(new_listNode)   # 結束則把表放回queue
            point_val += 1

        return res.next
       
# @lc code=end

