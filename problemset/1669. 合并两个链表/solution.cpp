
struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
  ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
    ListNode* removeStartNode = nullptr;
    ListNode* removeEndNode = nullptr;

    ListNode* t = list1;
    for (int i = 1;; i++) {
      if (a == i) {
        removeStartNode = t;
      }
      if (b == i) {
        removeEndNode = t->next->next;
        break;
      }
      t = t->next;
    }

    // delete
    t = removeStartNode->next;
    while (t->next != removeEndNode) {
      ListNode* t2 = t->next;
      delete t;
      t = t2;
    }

    // add
    removeStartNode->next = list2;
    t = list2;

    while (t->next != nullptr) {
      t = t->next;
    }

    t->next = removeEndNode;
    return list1;
  }
};