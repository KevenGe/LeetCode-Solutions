#include <iostream>
#include <queue>
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
  vector<vector<int>> levelOrderBottom(TreeNode *root) {
    vector<vector<int>> ans;

    if (root == nullptr) {
      return ans;
    }

    queue<TreeNode *> ques;
    int curLevelNum = 0;
    int nextLevelNum = 0;

    ques.push(root);
    nextLevelNum += 1;

    while (!ques.empty()) {
      if (curLevelNum == 0 && nextLevelNum != 0) {
        vector<int> v;
        ans.insert(ans.begin(), v);

        curLevelNum = nextLevelNum;
        nextLevelNum = 0;
      }

      TreeNode *node = ques.front();
      ques.pop();
      curLevelNum -= 1;

      ans[0].push_back(node->val);

      if (node->left != nullptr) {
        ques.push(node->left);
        nextLevelNum += 1;
      }

      if (node->right != nullptr) {
        ques.push(node->right);
        nextLevelNum += 1;
      }
    }

    return ans;
  }
};

int main() {
  TreeNode *root1 = new TreeNode(3);
  TreeNode *root2 = new TreeNode(9);
  TreeNode *root3 = new TreeNode(20);
  TreeNode *root4 = new TreeNode(15);
  TreeNode *root5 = new TreeNode(7);

  root1->left = root2;
  root1->right = root3;
  root3->left = root4;
  root3->right = root5;

  Solution so;
  for (auto t : so.levelOrderBottom(root1)) {
    for (auto b : t) {
      cout << b << " ";
    }
    cout << endl;
  }

  return 0;
}