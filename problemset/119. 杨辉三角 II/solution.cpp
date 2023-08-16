// LeetCode 119

#include <iostream>
#include <vector>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> ans;

    vector<int> rightSideView(TreeNode *root) {
        ans.clear();
        dfs(0, root);
        return ans;
    }

    void dfs(int deepth, TreeNode *root) {
        if (root) {
            if (ans.size() == deepth) {
                ans.push_back(root->val);
            } else {
                ans[deepth] = root->val;
            }
            dfs(deepth + 1, root->left);
            dfs(deepth + 1, root->right);
        }
    }
};


int main() {

    TreeNode *root1 = new TreeNode(1);
    TreeNode *root2 = new TreeNode(2);
    TreeNode *root3 = new TreeNode(3);
    TreeNode *root4 = new TreeNode(4);
    TreeNode *root5 = new TreeNode(5);

    root1->left = root2;
    root2->right = root5;
    root1->right = root3;
    root3->right = root4;

    Solution so;
    for (int x: so.rightSideView(root1)) {
        cout << x << endl;
    }

    return 0;
}