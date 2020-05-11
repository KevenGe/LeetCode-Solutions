/*
 * LeetCode 98. 验证二叉搜索树
 * Author: Keven Ge
 * Date: 2020-04-05
 */

#include <iostream>
#include <limits.h>

using namespace std;


//  Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isValidBST(TreeNode *root) {
        return dfs(root, LONG_MIN, LONG_MAX);
    }

    bool dfs(TreeNode *root, long min_limit, long max_limit) {
        if (root) {
            if (root->val > min_limit && root->val < max_limit) {
                if(dfs(root->left, min_limit, root->val) && dfs(root->right, root->val, max_limit)){
                    return true;
                }
            }
            return false;
        }
        return true;
    }
};

int main() {
    return 0;
}


