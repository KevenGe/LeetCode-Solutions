#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;


struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
	vector<int> postorderTraversal(TreeNode* root) {
		vector<int> ans;
		function<void(TreeNode*)> dfs = [&](TreeNode* node) {
			if (node == nullptr)
			{
				return;
			}
			dfs(node->left);
			dfs(node->right);
			ans.push_back(node->val);
		};
		dfs(root);
		return ans;
	}
};
