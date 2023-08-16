/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head)
        {
            ListNode* p = head;
            ListNode* q = head;
            do{
                p = p->next;
                q = q->next;
                
                if(p == NULL || q == NULL || q->next == NULL)
                {
                    return false;
                }

                q = q->next;
            }while(p != q);

            return true;
        }
        else
        {
            return false;
        }
    }
};