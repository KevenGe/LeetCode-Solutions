// 3
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int dp[128];
        fill(dp, dp + 128, -1);
        int ans = 0; // result
        int left_index = -1; // the left index of the s(array).
        for (int i = 0; i < s.length(); ++i) {
            int tmp = dp[int(s[i])];
            if (tmp > left_index) {
                left_index = tmp;
            }
            ans = max(ans, i - left_index);
            dp[int(s[i])] = i;
        }
        return ans;
    }
};


int main() {
    Solution so;
    cout << so.lengthOfLongestSubstring(" ") << endl;
    return 0;
}
