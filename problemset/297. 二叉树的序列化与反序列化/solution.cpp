#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode *root) {
        if (root) {
            return "[" + to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right) + "]";
        } else {
            return "";
        }
    }

    // Decodes your encoded data to tree.
    TreeNode *deserialize(string data) {
        if (data.empty()) {
            return nullptr;
        } else {
            vector<int> vec;
            int count = 0;
            for (int i = 1; i < data.size(); i++) {
                if (count == 0 && data[i] == ',') {
                    vec.push_back(i);
                    if (vec.size() == 2){
                        break;
                    }
                } else if (data[i] == '[') {
                    count += 1;
                } else if (data[i] == ']') {
                    count -= 1;
                }
            }
            string l = data.substr(1, vec[0] - 1);
            string m = data.substr(vec[0]+1, vec[1] -1 - vec[0]);
            string r = data.substr(vec[1]+1, data.size()-2 - vec[1]);
            TreeNode * root = new TreeNode(stoi(l));
            root->left = deserialize(m);
            root->right = deserialize(r);
            return root;
        }
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));

void runTest() {
    TreeNode *root1 = new TreeNode(1);
    TreeNode *root2 = new TreeNode(2);
    TreeNode *root3 = new TreeNode(3);
    TreeNode *root4 = new TreeNode(4);
    TreeNode *root5 = new TreeNode(5);

    root1->left = root2;
    root1->right = root3;
    root2->left = root4;
    root2->right = root5;

    Codec so;
    cout << so.serialize(root1) << endl;

}

int main() {
    runTest();
    return 0;
}