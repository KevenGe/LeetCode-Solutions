//
// Created by lenovo on 2020/6/8.
//

/**
 * 990. 等式方程的可满足性
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;


class Solution {
public:
    int par[26];
    int rank[26];

    int find(int i) {
        if (this->par[i] == i) {
            return i;
        } else {
            return this->par[i] = find(this->par[i]);
        }
    }

    void unionit(int a, int b) {
        a = this->find(a);
        b = this->find(b);
        if (this->rank[a] < this->rank[b]) {
            this->par[a] = b;
        } else {
            this->par[b] = a;
            if (this->rank[a] == this->rank[b]) {
                this->rank[a] += 1;
            }
        }
    }

    bool same(int a, int b) {
        return this->find(a) == this->find(b);
    }

    bool equationsPossible(vector <string> &equations) {
        for (int i = 0; i < 26; ++i) {
            this->par[i] = i;
            this->rank[i] = 0;
        }

        for (string equation: equations) {
            if (equation[1] == '=') {
                int a = int(equation[0] - 'a');
                int b = int(equation[3] - 'b');
                this->unionit(a, b);
            }
        }

        for (string equation: equations) {
            if (equation[1] == '!') {
                int a = int(equation[0] - 'a');
                int b = int(equation[3] - 'b');
                if (this->same(a, b)) {
                    return false;
                }
            }
        }

        return true;
    }
};

int main() {
    vector<string> vec;
    vec.push_back("a==b");
    vec.push_back("a!=b");

    Solution so;
    cout << so.equationsPossible(vec) << endl;
    return 0;
}