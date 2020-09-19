#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <climits>
#include <stack>

using namespace std;

/**
 * @brief 动态规划
 */
//class Solution {
//public:
//    static int longestValidParentheses(string s) {
//        if(s.size() < 2){
//            return 0;
//        }
//        vector<int> dp(s.size(), 0);
//        int ans = INT_MIN;
//        for (int i = 1; i < s.size(); ++i) {
//            if (s[i] == ')') {
//                if (s[i - 1] == '(') {
//                    if (i - 2 >= 0) {
//                        dp[i] = dp[i - 2] + 2;
//                    } else {
//                        dp[i] = 2;
//                    }
//                } else {
//                    if (i - dp[i - 1] - 1 >= 0) {
//                        if (s[i - dp[i - 1] - 1] == '(') {
//                            dp[i] = dp[i - 1] + 2;
//                            if (i - dp[i - 1] - 2 >= 0 && s[i - dp[i - 1] - 2] == ')') {
//                                dp[i] += dp[i - dp[i - 1] - 2];
//                            }
//                        }
//                    }
//                }
//            }
//            ans = max(ans, dp[i]);
//        }
//        return ans;
//    }
//};

/**
 * @brief 堆栈
 */
//
//
//

/**
 * @brief double point. left and right.
 */
class Solution {
public:
    static int longestValidParentheses(string s) {
        int ans = 0;

        int left = 0;
        int right = 0;


        // left to right
        for (char i : s) {
            if (i == '(') {
                left += 1;
            } else {
                right += 1;
            }

            if (right > left) {
                left = 0;
                right = 0;
            } else if (right == left) {
                ans = max(ans, right * 2);
            }
        }

        // right -> left
        left = 0;
        right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == '(') {
                left += 1;
            } else {
                right += 1;
            }

            if (right < left) {
                left = 0;
                right = 0;
            } else if (right == left) {
                ans = max(ans, right * 2);
            }
        }

        return ans;
    }
};


int main() {
    Solution so;
    cout << so.longestValidParentheses("((()())") << endl;
    return 0;
}