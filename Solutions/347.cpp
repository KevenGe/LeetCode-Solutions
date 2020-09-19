/**
 *  347.前 K 个高频元素
 *  @author KevenGe
 *  @date 2020-09-13
 */


#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>

using namespace std;

struct cmp {
    bool operator()(pair<int, int> p1, pair<int, int> p2) {
        return p1.second > p2.second;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int> &nums, int k) {
        unordered_map<int, int> occurrences;

        for (auto num:nums) {
            occurrences[num]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pri;
        for (auto x:occurrences) {
            if (pri.size() < k) {
                pri.push(x);
            } else {
                if (x.second > pri.top().second) {
                    pri.push(x);
                    pri.pop();
                }
            }
        }

        // get the answer
        vector<int> ans;
        while (!pri.empty()) {
            ans.emplace_back(pri.top().first);
            pri.pop();
        }
        return ans;
    }
};

int main() {
    return 0;
}