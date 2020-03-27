#include <iostream>
#include <string>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

//迭代方式
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *root = NULL;
        while (head)
        {
            if (root)
            {
                ListNode *tmp;
                tmp = head;
                head = head->next;
                tmp->next = root;
                root = tmp;
            }
            else
            {
                root = head;
                head = head->next;
                root->next = NULL;
            }
        }
        return root;
    }
};

// 递归方式
// class Solution
// {
// public:
//     ListNode *reverseList(ListNode *head)
//     {
//         ListNode *root = NULL;
//         reverseListHelper(root, head);
//         return root;
//     }

//     void reverseListHelper(ListNode *&root, ListNode *&head)
//     {
//         if (head)
//         {
//             if (root)
//             {
//                 ListNode *tmp = head;
//                 head = head->next;
//                 tmp->next = root;
//                 root = tmp;
//             }
//             else
//             {
//                 root = head;
//                 head = head->next;
//                 root->next = NULL;
//             }
//             reverseListHelper(root, head);
//         }
//     }
// };

int main()
{
    ListNode *root1 = new ListNode(1);
    ListNode *root2 = new ListNode(2);
    ListNode *root3 = new ListNode(3);
    ListNode *root4 = new ListNode(4);
    ListNode *root5 = new ListNode(5);
    root1->next = root2;
    root2->next = root3;
    root3->next = root4;
    root4->next = root5;

    ListNode *root111 = new ListNode(111);
    Solution so;
    root111 = so.reverseList(root1);
    return 0;
}