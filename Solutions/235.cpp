#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        if (root->val == p->val || root->val == q->val)
        {
            return root;
        }

        if (root->val > p->val)
        {
            if (root->val < q->val)
            {
                return root;
            }
            else
            {
                return lowestCommonAncestor(root->left, p, q);
            }
        }
        else
        {
            if (root->val < q->val)
            {
                return lowestCommonAncestor(root->right, p, q);
            }
            else
            {
                return root;
            }
        }
    }
};

int main()
{
    return 0;
}