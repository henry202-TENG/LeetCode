/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        struct ListNode *head = new ListNode();
        struct ListNode *curr = head;
        int digit = 0;
        while (l1 != nullptr || l2 != nullptr)
        {
            int temp = 0;
            struct ListNode *tempNode = new ListNode();
            if (l1 != nullptr && l2 != nullptr)
            {
                temp = l1->val + l2->val + digit;
                l1 = l1->next;
                l2 = l2->next;
            }
            else if (l1 == nullptr && l2 != nullptr)
            {
                temp = l2->val + digit;
                l2 = l2->next;
            }
            else
            {
                temp = l1->val + digit;
                l1 = l1->next;
            }
            digit = temp/10;
            tempNode->val = temp % 10;
            curr->next = tempNode;
            curr = curr->next;
        }

        if (digit > 0)
        {
            struct ListNode *tempNode = new ListNode();
            tempNode->val = digit;
            curr->next = tempNode;
            curr = curr->next;
        }
        return head->next;
    }
};
// @lc code=end

