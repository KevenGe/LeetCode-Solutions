//
// Created by lenovo on 2020/6/11.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <climits>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int> &T) {
        vector<int> res(T.size());
        int maps[101];
        fill(maps, maps + 101, INT_MAX);
        stack<int> stacks;
        stacks.push(INT_MAX);
        for (int i = T.size() - 1; i >= 0; --i) {
            // stack
            if (T[i] >=  stacks.top()) {
                stacks.pop();
                while (T[i] >= stacks.top()) {
                    stacks.pop();
                }
            }

            // map
            maps[T[i]] = i;

            if (stacks.top() == INT_MAX) {
                res[i] = 0;
            } else {
                res[i] = maps[stacks.top()] - maps[T[i]];
            }

            stacks.push(T[i]);
        }
        return res;
    }
};

int main() {
    vector<int> vec;
    vec.push_back(73);
    vec.push_back(74);
    vec.push_back(75);
    vec.push_back(71);
    vec.push_back(69);
    vec.push_back(72);
    vec.push_back(76);
    vec.push_back(73);

    Solution so;
    for (auto x: so.dailyTemperatures(vec)) {
        cout << x << endl;
    }

    return 0;
}
