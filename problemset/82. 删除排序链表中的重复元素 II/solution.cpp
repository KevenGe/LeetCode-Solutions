#include <set>

using namespace std;

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
  ListNode* deleteDuplicates(ListNode* head) {
    set<int> waitToDelete;

    // step 1
    set<int> occurToFind;
    ListNode* t = head;
    while (t != nullptr) {
      if (occurToFind.find(t->val) != occurToFind.end()) {
        waitToDelete.insert(t->val);
      } else {
        occurToFind.insert(t->val);
      }
      t = t->next;
    }

    // step 2
    ListNode* ans = head;
    if (ans == nullptr) {
      return nullptr;
    }

    while (ans != nullptr &&
           waitToDelete.find(ans->val) != waitToDelete.end()) {
      t = ans;
      ans = ans->next;

      delete t;
    }

    if (ans == nullptr) {
      return nullptr;
    }

    ListNode* prior = ans;
    while (prior->next != nullptr) {
      if (waitToDelete.find(prior->next->val) != waitToDelete.end()) {
        t = prior->next;
        prior->next = prior->next->next;
        delete t;
      } else {
        prior = prior->next;
      }
    }

    return ans;
  }
};