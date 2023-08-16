#include <iostream>
#include <string>
#include <map>
using namespace std;

// -------------------------------------------------------------------------- //

class Node
{
    char val;
    map<char, Node *> nextMap;

public:
    Node(char val_)
    {
        this->val = val_;
    }

    // 获取对应节点
    Node *getOrCreateNextNode(char val)
    {
        if (nextMap.find(val) != nextMap.end())
        {
            return nextMap.at(val);
        }
        else
        {
            Node *tmp = new Node(val);
            nextMap.insert(map<char, Node *>::value_type(val, tmp));
            return tmp;
        }
    }

    Node *getNextNode(char val)
    {
        if (nextMap.find(val) != nextMap.end())
        {
            return nextMap.at(val);
        }
        else
        {
            return nullptr;
        }
    }

    bool hasNextNodes()
    {
        return this->nextMap.size() != 0;
    }

    bool reachEnd()
    {
        return this->nextMap.find('$') != this->nextMap.end();
    }
};

class Trie
{
private:
    Node *head;

public:
    /** Initialize your data structure here. */
    Trie()
    {
        this->head = new Node('0');
    }

    /** Inserts a word into the trie. */
    void insert(string word)
    {
        Node *tmp = head;
        for (int i = 0; i < word.length(); i++)
        {
            tmp = tmp->getOrCreateNextNode(word[i]);
        }
        tmp->getOrCreateNextNode('$');
    }

    /** Returns if the word is in the trie. */
    bool search(string word)
    {
        Node *tmp = head;
        for (int i = 0; i < word.length(); i++)
        {
            tmp = tmp->getNextNode(word[i]);
            if (tmp == nullptr)
            {
                return false;
            }
        }

        return tmp->reachEnd();
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix)
    {
        Node *tmp = head;
        for (int i = 0; i < prefix.length(); i++)
        {
            tmp = tmp->getNextNode(prefix[i]);
            if (tmp == nullptr)
            {
                return false;
            }
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

// -------------------------------------------------------------------------- //

int main()
{
    Trie *t = new Trie();
    t->insert("app");
    cout << t->search("app") << endl;
    return 0;
}