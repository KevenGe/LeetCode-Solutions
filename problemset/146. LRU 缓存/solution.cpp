
/*
 * LeetCode 146
 * [LRU]
 * 哈希表和双向链表
 */

#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

// leetcode 146

struct Node {
    int val;
    Node *pre;
    Node *next;

    explicit Node(int val) {
        this->val = val;
        this->pre = nullptr;
        this->next = nullptr;
    }
};

class LRUCache {
public:
    int capacity;
    unordered_map<int, int> maps;
    // for delete
    Node *head;
    Node *tail;
    unordered_map<int, Node *> node_maps;

    explicit LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new Node(0);
        this->tail = this->head;
    }

    int get(int key) {
        if (maps.find(key) != maps.end()) {
            Node *tmp = this->node_maps[key];
            if (tmp->next != nullptr) {
                tmp->pre->next = tmp->next;
                tmp->next->pre = tmp->pre;
                this->tail->next = tmp;
                tmp->pre = this->tail;
                tmp->next = nullptr;
                this->tail = tmp;
            }
            return maps[key];
        }else{
            return -1;
        }
        return -1;
    }

    void put(int key, int value) {
        if (maps.find(key) != maps.end()) {
            maps[key] = value;

            Node *tmp = this->node_maps[key];
            if (tmp->next != nullptr) {
                tmp->pre->next = tmp->next;
                tmp->next->pre = tmp->pre;
                this->tail->next = tmp;
                tmp->pre = this->tail;
                tmp->next = nullptr;
                this->tail = tmp;
            }
        } else {
            if (maps.size() + 1 > this->capacity) {
                maps.erase(this->head->next->val);
                node_maps.erase(this->head->next->val);
                Node *tmp = this->head;
                this->head = this->head->next;
                delete tmp;
            }
            Node *tmp = new Node(key);
            this->tail->next = tmp;
            tmp->pre = this->tail;
            this->tail = tmp;
            node_maps.insert(unordered_map<int, Node *>::value_type(key, tmp));
            maps.insert(unordered_map<int, int>::value_type(key, value));
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


int main() {
    LRUCache cache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1) << endl;       // 返回  1
    cache.put(3, 3);    // 该操作会使得密钥 2 作废
    cout << cache.get(2) << endl;       // 返回 -1 (未找到)
    cache.put(4, 4);    // 该操作会使得密钥 1 作废
    cout << cache.get(1) << endl;       // 返回 -1 (未找到)
    cout << cache.get(3) << endl;       // 返回  3
    cout << cache.get(4) << endl;       // 返回  4

    return 0;
}
