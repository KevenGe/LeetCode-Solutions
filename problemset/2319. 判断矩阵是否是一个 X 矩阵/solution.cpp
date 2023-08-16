#include <vector>

using namespace std;

class Solution {
 public:
  bool checkXMatrix(vector<vector<int>>& grid) {
    int n = grid.size();

    auto isShouldBeZero = [&](int i, int j) -> bool {
      return !(i == j || i + j == n - 1);
    };

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if ((isShouldBeZero(i, j) && grid[i][j] != 0) ||
            (!isShouldBeZero(i, j) && grid[i][j] == 0)) {
          return false;
        }
      }
    }

    return true;
  }
};