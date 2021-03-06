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
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if (p == nullptr) {
            return q == nullptr;
        } else {
            if(q == nullptr){
                return false;
            }else{
                if( p->val == q->val){
                    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
                } else{
                    return false;
                }
            }
        }
    }
};

int main() {
    return 0;
}