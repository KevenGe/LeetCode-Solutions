//
// Created by lenovo on 2020-07-03.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int> > dp(201, vector<int>(201));

        if(word1.length() == 0){
            return word2.length();
        }

        if(word2.length() == 0){
            return word1.length();
        }


        for (int i = 0; i <= word1.length(); ++i) {
            dp[i][0] = i;
        }

        for (int j = 0; j <= word2.length(); ++j) {
            dp[0][j] = j;
        }

        for (int i = 1; i <= word1.length(); ++i) {
            for (int j = 1; j <= word2.length(); ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = 1 + min(dp[i][j - 1], min(dp[i - 1][j], dp[i-1][j-1] - 1));
                } else {
                    dp[i][j] = 1 + min(dp[i][j - 1], min(dp[i - 1][j], dp[i-1][j-1]));
                }
            }
        }

        return dp[word1.length()][word2.length()];
    }
};

int main() {
    string a, b;
    cin >> a >> b;
    Solution so;
    cout << so.minDistance(a, b) << endl;
    return 0;
}