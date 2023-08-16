#include <iostream>
#include <limits.h>
#include <algorithm>
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
    int ans;
    int diameterOfBinaryTree(TreeNode *root)
    {
        ans = 0;

        dfs(root);
        return ans;
    }

    int dfs(TreeNode *root)
    {
        if (root)
        {
            int l = dfs(root->left);
            int r = dfs(root->right);
            ans = max(ans, l + r);
            return max(l, r) + 1;
        }
        else
        {
            return 0;
        }
        return -1;
    }
};

int main()
{
    return 0;
}