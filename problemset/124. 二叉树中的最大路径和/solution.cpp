#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
private:
    int maxs = INT_MIN;
public:
    int maxPathSum(TreeNode *root) {
        helper(root);
        return this->maxs;
    }

    int helper(TreeNode *root) {
        if (root) {
            int l = helper(root->left);
            int r = helper(root->right);

            int tmp = root->val;
            if(l <= 0){
                if (r <= 0){
                    this->maxs = max(this->maxs, root->val);
                    return root->val;
                }else{
                    this->maxs = max(this->maxs, root->val + r);
                    return root->val +r;
                }
            }else{
                if(r <= 0){
                    this->maxs = max(this->maxs, root->val + l);
                    return root->val +l;
                }else{
                    this->maxs = max(this->maxs, root->val + l + r);
                    return max(root->val + l, root->val + r);
                }
            }
        }else {
            return INT_MIN;
        }
    }
};

int main() {
    cout << "ok" << endl;
    return 0;
}
