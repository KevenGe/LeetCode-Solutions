//
// Created by lenovo on 2020/6/25.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) {
            vector<int> ansT;
            ansT.push_back(1);
            return ansT;
        } else {
            vector<int> ansT = getRow(rowIndex - 1);
            vector<int> ans(rowIndex + 1);
            ans[0] = 1;
            ans[rowIndex] = 1;
            for (int i = 0; i < ansT.size()-1; ++i) {
                ans[i + 1] = ansT[i] + ansT[i + 1];
            }
            return ans;
        }
    }
};

int main() {
    Solution so;
    for (auto x:so.getRow(3)) {
        cout << x << endl;
    }
    return 0;
}