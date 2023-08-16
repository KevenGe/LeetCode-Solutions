#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int surfaceArea(vector<vector<int>> &grid) {
        int ans = 0;
        if (grid.empty()) {
            return 0;
        }

        // Search for it.
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] > 0) {
                    ans += 2;
                    //up
                    if (i == 0) {
                        ans += grid[i][j];
                    } else if (grid[i - 1][j] < grid[i][j]) {
                        ans += grid[i][j] - grid[i - 1][j];
                    }

                    //down
                    if (i == grid.size() - 1) {
                        ans += grid[i][j];
                    } else if (grid[i + 1][j] < grid[i][j]) {
                        ans += grid[i][j] - grid[i + 1][j];
                    }

                    //left
                    if (j == 0) {
                        ans += grid[i][j];
                    } else if (grid[i][j - 1] < grid[i][j]) {
                        ans += grid[i][j] - grid[i][j - 1];
                    }

                    //right
                    if (j == grid[0].size() - 1) {
                        ans += grid[i][j];
                    } else if (grid[i][j + 1] < grid[i][j]) {
                        ans += grid[i][j] - grid[i][j + 1];
                    }
                }
            }
        }
        return ans;
    }
};


int main() {
    vector<vector<int> > vec;
    vector<int> row1;
    row1.push_back(2);
    vec.push_back((row1));
    Solution so;
    cout << so.surfaceArea(vec) << endl;
    return 0;
}
