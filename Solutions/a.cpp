#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int val;
    Node *next;

    Node(int val_) {
        val = val_;
        next = nullptr;
    }
};

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<Node *> nodes(n + 1, nullptr);
    vector<Node *> nodeTails(n + 1, nullptr);


    for (int i = 1; i <= n; i++) {
        Node *node = new Node(i);
        nodes[i] = node;
        nodeTails[i] = node;
    }

    {
        while (m--) {
            int a, b;
            cin >> a >> b;
            if (a == b || nodes[b] == nullptr) {
                continue;
            } else if (nodes[a] == nullptr) {
                nodes[a] = nodes[b];
                nodes[b] = nullptr;
                nodeTails[a] = nodeTails[b];
                nodeTails[b] = nullptr;
            } else {
                nodeTails[a]->next = nodes[b];
                nodes[b] = nullptr;
                nodeTails[a] = nodeTails[b];
                nodeTails[b] = nullptr;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        Node *tmp = nodes[i];
        while (tmp) {
            cout << tmp->val << " ";
            tmp = tmp->next;
        }
        cout << endl;
    }

    return 0;
}