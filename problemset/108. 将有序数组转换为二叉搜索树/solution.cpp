#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &nums) {
        return helper(nums, 0, nums.size()-1);
    }

    TreeNode*helper(vector<int>&nums, int l, int r){
        if(l > r){
            return nullptr;
        }

        int mid = (l+r)/2;
        TreeNode*p = new TreeNode(nums[mid]);
        p->left = helper(nums, l, mid-1);
        p->right = helper(nums, mid+1, r);
        return p;
    }
};

int main() {
    return 0;
}