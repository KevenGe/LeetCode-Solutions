#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool> > dp(s.size() + 1, vector<bool>(p.size() + 1));

        // initial
        dp[0][0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            dp[i][0] = false;
        }
        for (int j = 2; j <= p.size(); ++j) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            } else {
                dp[0][j] = false;
            }
        }

//        for (int i = 0; i <= s.size(); i++) {
//            for (int j = 0; j <= p.size(); j++) {
//                cout << dp[i][j] << " ";
//            }
//            cout << endl;
//        }



        // dynamic process
        char extraPoint = '.'; ///< 这是一个特殊字符，用来存储上一个‘.’代表的字符

        for (int i = 1; i <= s.size(); i++) {
            for (int j = 1; j <= p.size(); j++) {
                if (p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                    extraPoint = s[i - 1];
                } else if (p[j - 1] == '*') {
                    if (j - 2 >= 0) {
                        if (p[j - 2] == '.') {
                            dp[i][j] = dp[i][j - 2] || (s[i - 1] == extraPoint && dp[i - 1][j]);
                        } else {
                            dp[i][j] = dp[i][j - 2] || (s[i - 1] == p[j - 2] && dp[i - 1][j]);
                        }
                    }
                } else {
                    dp[i][j] = s[i - 1] == p[j - 1] ? dp[i - 1][j - 1] : false;
                }
            }
        }

        return dp[s.size()][p.size()];
    }
};

int main() {
    string s, p;
    Solution so;

    ///////////////////////////////////////////////////
    s = "aab";
    p = "c*a*b";
    cout << so.isMatch(s, p) << endl;

    return 0;
}