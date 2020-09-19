//
// Created by lenovo on 2020-08-02.
//

#include <iostream>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void flatten(TreeNode *root) {
        helper(root);
    }

    /**
     *
     * @param root
     * @return Final TreeNode
     */
    TreeNode *helper(TreeNode *root) {
        if (root) {
            if (root->left) {
                TreeNode *l = helper(root->left);
                TreeNode *r = helper(root->right);
                TreeNode *r_head = root->right;

                root->right = root->left;
                root->left = nullptr;

                l->right = r_head;

                if (root->right) {
                    return r;
                } else {
                    return l;
                }
            }else{
                if (root->right) {
                    TreeNode *r = helper(root->right);
                    return r;
                } else {
                    return  root;
                }
            }
        } else {
            return nullptr;
        }
    }

};

int main(){
    return 0;
}