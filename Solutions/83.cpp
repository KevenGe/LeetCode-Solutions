
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (head == nullptr)
        {
            return nullptr;
        }

        ListNode *preNode = nullptr;
        ListNode *curNode = head;

        while (curNode != nullptr && curNode->next != nullptr)
        {
            preNode = curNode;
            curNode = curNode->next;

            if (curNode == nullptr)
            {
                break;
            }

            if (curNode->val == preNode->val)
            {
                ListNode *tmpNode = curNode;
                preNode->next = curNode->next;
                delete tmpNode;
                curNode = preNode;
            }
        }

        return head;
    }
};