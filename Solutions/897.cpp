#include <iostream>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
    TreeNode *beforeNode = nullptr;
    TreeNode *headNode = nullptr;

public:
    TreeNode *increasingBST(TreeNode *root)
    {
        mid(root);
        return headNode;
    }

    void mid(TreeNode *root)
    {
        if (root)
        {
            mid(root->left);

            if (headNode == nullptr)
            {
                headNode = root;
                headNode->left = nullptr;
                beforeNode = headNode;
            }
            else
            {
                beforeNode->right = root;
                beforeNode = beforeNode->right;
                beforeNode->left = nullptr;
            }

            mid(root->right);
        }
    }
};

int main()
{
    return 0;
}