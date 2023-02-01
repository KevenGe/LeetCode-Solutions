#include <functional>
#include <map>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
 public:
  TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
    map<int, int> inorderIndexMap;
    for (int i = 0; i < inorder.size(); i++) {
      inorderIndexMap[inorder[i]] = i;
    }

    function<TreeNode *(int, int, int, int)> buildTreeInsider =
        [&](int inorderBegin, int inorderEnd, int postorderBegin,
            int postorderEnd) -> TreeNode * {
      if (inorderEnd <= inorderBegin) {
        return nullptr;
      }

      int rootVal = postorder[postorderEnd - 1];
      TreeNode *root = new TreeNode(rootVal);

      // left
      int inorderRootIndex = inorderIndexMap[rootVal];
      root->left =
          buildTreeInsider(inorderBegin, inorderRootIndex, postorderBegin,
                           postorderBegin + (inorderRootIndex - inorderBegin));
      root->right = buildTreeInsider(
          inorderRootIndex + 1, inorderEnd,
          postorderBegin + (inorderRootIndex - inorderBegin), postorderEnd - 1);

      return root;
    };

    return buildTreeInsider(0, inorder.size(), 0, postorder.size());
  }
};