/*
 * LeetCode 226
 *
 * Date: 2020-05-03
 * Author: Keven Ge
 */
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
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
    TreeNode *invertTree(TreeNode *root) {
        if(root){
//            TreeNode *tmp = root->left;
//            root->left = root->right;
//            root->right = tmp;
//
//            root->left = invertTree(root->left);
//            root->right = invertTree(root->right);

                TreeNode *tmp = root->left;
                root->left = invertTree(root->right);
                root->right = invertTree(tmp);
            return root;
        }
        return NULL;
    }
};


int main() {
    return 0;
}
