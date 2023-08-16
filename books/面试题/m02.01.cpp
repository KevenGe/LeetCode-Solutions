//
// Created by lenovo on 2020/6/26.
//

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
#include <unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode *removeDuplicateNodes(ListNode *head) {
        unordered_set<int> sets;
        ListNode * t = head;
        ListNode * p = nullptr;
        while(t != nullptr){
            if(sets.find(t->val) != sets.end()){
                p->next = t->next;
                delete t;
                t = p->next;
            }else{
                sets.insert(t->val);
                p = t;
                t = t->next;
            }
        }
        return head;
    }
};

int main() {
    return 0;
}