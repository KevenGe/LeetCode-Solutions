#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr)
    {
    }
    ListNode(int x) : val(x), next(nullptr)
    {
    }
    ListNode(int x, ListNode *next) : val(x), next(next)
    {
    }
};

class Solution
{
  public:
    ListNode *doubleIt(ListNode *head)
    {
        stack<int> st;
        while (head != nullptr)
        {
            st.push(head->val);
            head = head->next;
        }

        ListNode *newHead = nullptr;
        int add = 0;
        while (!st.empty())
        {
            int s = st.top() * 2 + add;
            st.pop();
            add = s / 10;
            s = s % 10;

            if (newHead == nullptr)
            {
                newHead = new ListNode(s);
                newHead->next = nullptr;
            }
            else
            {
                ListNode *newNode = new ListNode(s);
                newNode->next = newHead;
                newHead = newNode;
            }
        }
        if (add != 0)
        {
            ListNode *newNode = new ListNode(add);
            newNode->next = newHead;
            newHead = newNode;
        }
        return newHead;
    }
};

int main()
{
    return 0;
}