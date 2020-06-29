/*
 * LeetCode 460
 * LFU
 */

#include <iostream>
#include <unordered_map>
#include <map>

using namespace std;

// leetcode 460

struct Node {
    int val = 0;
    int times = 0;
    Node *pre = nullptr;
    Node *next = nullptr;
};

struct Level_Node {
    int times = 0;
    Node *node = nullptr;
    Level_Node *level_next = nullptr;

    Level_Node() {
        this->node = new Node();
    }
};

class LFUCache {
public:
    int capacity;
    unordered_map<int, int> maps;
    unordered_map<int, Node *> node_maps;
    unordered_map<int, Node *> level_node_maps;

    explicit LFUCache(int capacity) {
        this->capacity = capacity;
        this->maps.clear();
        this->node_maps.clear();
        this->level_node_maps.clear();
    }

    int get(int key) {
        if (this->maps.find(key) != this->maps.end()) {
            return this->maps[key];
        } else {
            return -1;
        }
    }

    void put(int key, int value) {
        if (this->maps.find(key) != this->maps.end()) {
            this->maps[key] = value;

            auto *node = this->node_maps[key];

        } else {
            this->maps.insert(unordered_map<int, int>::value_type(key, value));

            Node *node = new Node();
            node->val = key;

            this->node_maps.insert(unordered_map<int, Node *>::value_type(key, node));
            if (this->level_node_maps.find(1) == this->level_node_maps.end()) {
                Node *tmp = new Node();
                this->level_node_maps.insert(unordered_map<int, Node *>::value_type(key, tmp));

                auto *head = this->level_node_maps[key];
                head->next = node;
                head->pre = node;
                node->pre = head;
                node->next = head;
            } else {
                auto *head = this->level_node_maps[key];
                node->next = head->next;
                node->pre = head;
                head->next->pre = node;
                head->next = node;
            }
        }
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


int main() {
    return 0;
}
