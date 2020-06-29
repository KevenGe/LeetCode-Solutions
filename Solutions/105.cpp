/*
 * LeetCode 105. 从前序与中序遍历序列构造二叉树
 *
 */

#include <iostream>
#include <vector>

using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return this->helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }

    TreeNode *helper(vector<int> &preorder, int pl, int pr, vector<int> &inorder, int il, int ir) {
        if (pr - pl < 0) {
            return nullptr;
        }

        //

        auto *tmp = new TreeNode(preorder[pl]);

        int i = 0;
        for (i = il; i <= ir; i++) {
            if (inorder[i] == preorder[pl]) {
                break;
            }
        }

        tmp->left = this->helper(preorder, pl + 1, pl + (i - il), inorder, il, i - 1);
        tmp->right = this->helper(preorder, pl + (i - il) + 1, pr, inorder, i + 1, ir);
        return tmp;
    }
};

int main() {
    vector<int> preorder;
    preorder.push_back(3);
    preorder.push_back(9);
    preorder.push_back(20);
    preorder.push_back(15);
    preorder.push_back(7);

    vector<int> inorder;
    inorder.push_back(9);
    inorder.push_back(3);
    inorder.push_back(15);
    inorder.push_back(20);
    inorder.push_back(7);

    Solution so;
    so.buildTree(preorder, inorder);

    return 0;
}