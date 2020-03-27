/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution
{
public:
	bool isSymmetric(TreeNode* root)
	{
		if (root == NULL)
		{
			return true;
		}
		else
		{
			return isMirror(root->left, root->right);
		}
	}

	bool isMirror(TreeNode* node1, TreeNode* node2)
	{
		if (node1 == NULL && node2 == NULL)
		{
			return true;
		}
		else if (node1 == NULL || node2 == NULL) {
			return false;
		}
		else
		{
			return (node1->val == node2->val)
				&& isMirror(node1->left, node2->right)
				&& isMirror(node1->right, node2->left);

		}
	}
};