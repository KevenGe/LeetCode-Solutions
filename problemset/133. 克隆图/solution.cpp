#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node *> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node *>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node *>();
    }

    Node(int _val, vector<Node *> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    unordered_set<int> sets;
    unordered_map<int, Node *> maps;

    Node *cloneGraph(Node *node) {
        if (node != nullptr) {
            if (maps.find(node->val) != maps.end()) {
                return maps[node->val];
            } else {
                Node * t = new Node(node->val);
                maps.insert(unordered_map<int, Node*>::value_type(node->val, t));
                for(auto next_node: node->neighbors){
                    t->neighbors.push_back(cloneGraph(next_node));
                }
                return t;
            }
        }
        return nullptr;
    }
};

int main() {
    return 0;
}
