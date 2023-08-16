#include <iostream>
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
    TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2)
    {
        TreeNode *root;
        mergeTreesHelper(root, t1, t2);
    }

    void mergeTreesHelper(TreeNode *root, TreeNode *left, TreeNode *right)
    {
        if (left == NULL)
        {
            if (right == NULL)
            {
                root = NULL;
            }
            else
            {
                root = new TreeNode(right->val);
                mergeTreesHelper(root->left, NULL, right->left);
                mergeTreesHelper(root->right, NULL, right->right);
            }
        }
        else
        {
            if (right == NULL)
            {
                root = new TreeNode(left->val);
                mergeTreesHelper(root->left, left->left, NULL);
                mergeTreesHelper(root->right, left->right, NULL);
            }
            else
            {
                root = new TreeNode(left->val + right->val);
                mergeTreesHelper(root->left, left->left, right->left);
                mergeTreesHelper(root->right, left->right, left->left);
            }
        }
    }
};

int main()
{
    return 0;
}