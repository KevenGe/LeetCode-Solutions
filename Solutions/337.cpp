#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

struct Res {
    int val1;
    int val2;

    Res(int val1, int val2) : val1(val1), val2(val2) {}

    int max(){
        return ::max(val1, val2);
    }
};

class Solution {
public:
    int rob(TreeNode *root) {
        Res resRes = helper(root);
        return max(resRes.val1, resRes.val2);
    }

    Res helper(TreeNode *root) {
        if (root) {
            Res resLeft = helper(root->left);
            Res resRight = helper(root->right);
            return {
                root->val + resLeft.val2 + resRight.val2,
                resLeft.max() + resRight.max()
            };
        } else {
            return {0, 0};
        }
    }
};

int main() {

    auto * root1 = new TreeNode(4);
    auto * root2 = new TreeNode(1);
    auto * root3 = new TreeNode(2);
    auto * root4 = new TreeNode(3);

    root1->left = root2;
    root2->left = root3;
    root3->left = root4;

    Solution so;
    cout << so.rob(root1) << endl;

    return 0;
}