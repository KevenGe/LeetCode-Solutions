#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid) {

        if (obstacleGrid.size() == 0 || obstacleGrid[0].size() == 0) {
            return 0;
        }

        if (obstacleGrid.size() == 1 && obstacleGrid[0].size() == 1) {
            return !obstacleGrid[0][0];
        }

        if(obstacleGrid[0][0] > 0 || obstacleGrid[obstacleGrid.size() - 1][obstacleGrid[0].size() - 1] > 0){
            return 0;
        }

        obstacleGrid[0][0] = -1;
        for (int i = 1; i < obstacleGrid.size(); i++) {
            if (obstacleGrid[i][0] == 0) {
                obstacleGrid[i][0] = obstacleGrid[i - 1][0] > 0 ? 0 : obstacleGrid[i - 1][0];
            }
        }

        for (int i = 1; i < obstacleGrid[0].size(); i++) {
            if (obstacleGrid[0][i] == 0) {
                obstacleGrid[0][i] = obstacleGrid[0][i - 1] > 0 ? 0 : obstacleGrid[0][i - 1];
            }
        }

//        for (int i = 0; i < obstacleGrid.size(); i++) {
//            for (int j = 0; j < obstacleGrid.size(); j++) {
//                cout << obstacleGrid[i][j] << " ";
//            }
//            cout << endl;
//        }

        for (int i = 1; i < obstacleGrid.size(); i++) {
            for (int j = 1; j < obstacleGrid.size(); j++) {
                if (obstacleGrid[i][j] == 0) {
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j] > 0 ? 0 : obstacleGrid[i - 1][j];
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1] > 0 ? 0 : obstacleGrid[i][j - 1];
                }
            }
        }

//        for (int i = 0; i < obstacleGrid.size(); i++) {
//            for (int j = 0; j < obstacleGrid.size(); j++) {
//                cout << obstacleGrid[i][j] << " ";
//            }
//            cout << endl;
//        }
        return -obstacleGrid[obstacleGrid.size() - 1][obstacleGrid[0].size() - 1];
    }
};

int main() {
    return 0;
}