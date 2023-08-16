/*
 * LeetCode 983. 最低票价
 * Author: Keven Ge
 * Date: 2020-05-06
 */

#include <iostream>
#include <vector>
#include <climits>
#include <unordered_set>
#include <algorithm>
#include <string>
#include <cwchar>

using namespace std;

class Solution {
private:
    vector<int> days, costs, dp;
    int dur[3] = {1, 7, 30};
public:
    int mincostTickets(vector<int> &days, vector<int> &costs) {
        this->days = days;
        this->costs = costs;
        this->dp.assign(days.size(), INT_MAX);
        return dfs(0);
    }

    int dfs(int i) {
        if (i >= days.size()) {
            return 0;
        } else if (this->dp[i] != INT_MAX) {
            return dp[i];
        } else {
            for (int k = 0; k < 3; ++k) {
                int j = i;
                while (j < days.size() && days[j] < days[i] + dur[k]) {
                    ++j;
                }
                dp[i] = min(dp[i], this->costs[k] + dfs(j));
            }
        }
        return dp[i];
    }

};

int main() {
    cout << "hello" << endl;
    return 0;
}
