#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL)
    {
    }
};

class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {
        if (head == NULL)
        {
            return NULL;
        }

        ListNode *p1 = head;
        ListNode *p2 = head->next;

        while (p2 != NULL)
        {
            if (p2->next != NULL)
            {
                if (p2->next->next != NULL)
                {
                    p2 = p2->next->next;
                    p1 = p1->next;
                }
                else
                {
                    p1 = p1->next;
                    break;
                }
            }
            else
            {
                p1 = p1->next;
                break;
            }
        }
        return p1;
    }
};

int main()
{
    return 0;
}