/*
 * LeetCode 572. 另一个树的子树
 * Author: Keven Ge
 * Date: 2020-05-07
 */

#include <iostream>

using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool isSubtree(TreeNode *s, TreeNode *t) {
        if (s != nullptr && t != nullptr) {
            if (s->val == t->val) {
                if (same(s, t)) {
                    return true;
                }
            }
            return isSubtree(s->left, t) || isSubtree(s->right, t);
        }
        return false;
    }

    bool same(TreeNode *s, TreeNode *t) {
        if (s == NULL && t == NULL) {
            return true;
        } else if (s != NULL && t != NULL) {
            if (s->val == t->val) {
                cout << same(s->left, t->left) << same(s->right, t->right) << endl;
                return same(s->left, t->left) && same(s->right, t->right);
            }
        }
        return false;
    }
};


int main() {
    TreeNode *root1 = new TreeNode(3);
    TreeNode *root2 = new TreeNode(4);
    TreeNode *root3 = new TreeNode(5);
    TreeNode *root4 = new TreeNode(1);
    TreeNode *root5 = new TreeNode(2);

    root1->left = root2;
    root2->left = root4;
    root2->right = root5;
    root1->right = root3;


    TreeNode *root23 = new TreeNode(4);
    TreeNode *root24 = new TreeNode(1);
    TreeNode *root25 = new TreeNode(2);

    root23->left = root24;
    root23->right = root25;

    Solution so;

    cout << so.isSubtree(root1, root23) << endl;
    return 0;
}
