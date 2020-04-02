#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

// LeetCode 739

class Solution {
public:
    vector<int> dailyTemperatures(vector<int> &T) {
        unsigned temp[101] = {0};
        vector<int> ans(T.size());
        stack<int> stacks;
        for (int i = T.size() - 1; i >= 0; --i) {
            if (stacks.empty()) {
                ans[i] = 0;
                temp[T[i]] = i;
                stacks.push(T[i]);
            } else if (T[i] < stacks.top()) {
                ans[i] = temp[stacks.top()] - i;
                stacks.push(T[i]);
                temp[T[i]] = i;
            } else {
                while(!stacks.empty() && T[i] >= stacks.top()){
                    stacks.pop();
                }
                if(stacks.empty()){
                    ans[i] = 0;
                    temp[T[i]] = i;
                    stacks.push(T[i]);
                }else{
                    ans[i] = temp[stacks.top()] - i;
                    stacks.push(T[i]);
                    temp[T[i]] = i;
                }
            }
        }
        return ans;
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
    for(auto x : so.dailyTemperatures(vec)){
        cout << x << endl;
    }
    return 0;
}
