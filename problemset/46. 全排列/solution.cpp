#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    static bool isMatch(string s, string p) {
        vector<vector<bool> > dp(s.size() + 1, vector<bool>(p.size() + 1));

        // initial
        dp[0][0] = true;
        for (int i = 1; i <= s.size(); i++) {
            dp[i][0] = false;
        }
        for (int i = 1; i <= p.size(); i++) {
            dp[0][i] = p[i-1] == '*' ? dp[0][i - 1] : false;
        }

        // show
//        for (int i = 0; i <= s.size(); i++) {
//            for (int j = 0; j <= p.size(); j++) {
//                cout << dp[i][j] <<" ";
//            }
//            cout << endl;
//        }


        // dp
        for (int i = 1; i <= s.size(); i++) {
            for (int j = 1; j <= p.size(); j++) {
                if (p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else {
                    dp[i][j] = (s[i - 1] == p[j - 1]) && dp[i - 1][j - 1];
                }
            }
        }

        return dp[s.size()][p.size()];
    }
};

int main() {
    /***************************************/
    string s = "aa";
    string b = "*";

    Solution so;
    cout << Solution::isMatch(s, b) << endl;

    return 0;
}