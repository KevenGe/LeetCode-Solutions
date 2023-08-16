//
// Created by lenovo on 2020/6/21.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
private:
    vector<int> ans;
public:
    vector<int> reversePrint(ListNode *head) {
        this->ans.clear();
        this->helper(head);
        reverse(ans.begin(), ans.end());
        return ans;
    }

    void helper(ListNode *root) {
        if(root){
            this->ans.push_back(root->val);
            this->helper(root->next);
        }
    }
};

int main() {
    return 0;
}
