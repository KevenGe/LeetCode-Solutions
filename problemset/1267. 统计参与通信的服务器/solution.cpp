#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution {
 public:
  int countServers(vector<vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();

    vector<set<int>> rowSet(m);
    vector<set<int>> colSet(n);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == 1) {
          rowSet[i].insert(j);
          colSet[j].insert(i);
        }
      }
    }
    int ans = 0;
    for (int i = 0; i < m; i++) {
      if (rowSet[i].size() >= 2) {
        ans += rowSet[i].size();
      }
    }
    for (int j = 0; j < n; j++) {
      if (colSet[j].size() >= 2) {
        ans += colSet[j].size();
        for (auto i : colSet[j]) {
          if (rowSet[i].size() >= 2) {
            ans -= 1;
          }
        }
      }
    }
    return ans;
  }
};

int main() {
  Solution so;
  vector<vector<int>> grid = {{1, 0}, {0, 1}};
  cout << so.countServers(grid) << endl;
  return 0;
}