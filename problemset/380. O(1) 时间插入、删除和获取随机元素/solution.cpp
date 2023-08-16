#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <time.h>

using namespace std;

class RandomizedSet {
private:
    vector<int> vec;
    unordered_map<int, int> maps;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        srand(time(0));
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (maps.find(val) == maps.end()) {
            vec.push_back(val);
            maps.emplace(val, vec.size() - 1);
            return true;
        } else {
            return false;
        }
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(maps.find(val) == maps.end()){
            return false;
        }else{
            vec[maps[val]] = vec.back();
            maps[vec.back()] = maps[val];
            vec.pop_back();
            maps.erase(val);
            return true;
        }
    }

    /** Get a random element from the set. */
    int getRandom() {

        return vec[rand() % vec.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

int main() {
    return 0;
}