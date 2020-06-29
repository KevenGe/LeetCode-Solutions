#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        if(root == nullptr){
            return true;
        }
        return isSymmetricHelper(root->left, root->right);
    }
    bool isSymmetricHelper(TreeNode *l, TreeNode *r) {
        if (l == nullptr && r == nullptr) {
            return true;
        } else if ((l != nullptr && r == nullptr) || (l == nullptr && r != nullptr)) {
            return false;
        } else {
            if (l->val == r->val) {
                return isSymmetricHelper(l->left, r->right) && isSymmetricHelper(l->right, r->left);
            } else {
                return false;
            }
        }
    }
};

int main() {
    return 0;
}
