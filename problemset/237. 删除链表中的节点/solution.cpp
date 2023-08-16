#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    void deleteNode(ListNode *node)
    {
        node->val = node->next->val;
        while (node->next->next != nullptr)
        {
            node = node->next;
            node->val = node->next->val;
        }

        node->next = nullptr;
    }
};

int main()
{
    return 0;
}