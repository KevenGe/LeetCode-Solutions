/*
    这个是力扣《剑指offer》的第七题
    根据前序遍历和后序遍历完成二叉树的构建！
*/

#include <iostream>
#include <vector>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        TreeNode *root = NULL;
        buildTreeHelper(root, preorder, 0, preorder.size(), inorder, 0, inorder.size());
        return root;
    }
    void buildTreeHelper(TreeNode *&root, vector<int> &preorder, int pl, int pt, vector<int> &inorder, int il, int ir)
    {

        if (pl < pt)
        {
            int root_num = preorder[pl];
            if (root == NULL)
            {
                root = new TreeNode(root_num);
            }

            int inorder_root_index = -1;
            for (int i = il; i < ir; ++i)
            {
                if (inorder[i] == root_num)
                {
                    inorder_root_index = i;
                    break;
                }
            }
            buildTreeHelper(root->left, preorder, pl + 1, pl + 1 + (inorder_root_index - il), inorder, il, inorder_root_index);
            buildTreeHelper(root->right, preorder, pl + 1 + (inorder_root_index - il), pt, inorder, inorder_root_index + 1, ir);
        }
    }
};

int main()
{
    vector<int> pre;
    pre.push_back(3);
    pre.push_back(9);
    pre.push_back(20);
    pre.push_back(15);
    pre.push_back(7);

    vector<int> in;
    in.push_back(9);
    in.push_back(3);
    in.push_back(15);
    in.push_back(20);
    in.push_back(7);
    
    Solution so;

    TreeNode *root =  so.buildTree(pre,in);
    
    return 0;
}