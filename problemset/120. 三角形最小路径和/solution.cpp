#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
 public:
  int minimumTotal(vector<vector<int>>& triangle) {
    // step 1
    vector<int> dp = triangle[triangle.size() - 1];

    for (int i = triangle.size() - 2; i >= 1; i -= 1) {
      for (int j = 0; j < i + 1; j++) {
        dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j];
      }
    }

    if (triangle.size() >= 2) {
      dp[0] = min(dp[0], dp[1]) + triangle[0][0];
    }

    return dp[0];
  }
};

int main() {
  vector<vector<int>> triangle = {{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}};

  Solution so;
  cout << so.minimumTotal(triangle) << endl;

  return 0;
}