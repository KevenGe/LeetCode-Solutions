#include <iostream>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    static bool hasPathSum(TreeNode *root, int sum) {
        if (root == nullptr) {
            return false;
        } else {
            sum -= root->val;

            if(root->left == nullptr && root->right == nullptr){
                return sum ==0;
            }

            if(root->left){
                if(hasPathSum(root->left, sum)){
                    return true;
                }
            }

            if(root->right){
                if(hasPathSum(root->right, sum)){
                    return true;
                }
            }

            return false;
        }
    }
};

int main() {
    return 0;
}