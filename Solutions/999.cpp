#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

//999

class Solution {
public:
    int numRookCaptures(vector<vector<char>> &board) {
        int x = 0;
        int y = 0;
        for (int i = 0; i < board.size(); ++i) {
            bool flag = false;
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == 'R') {
                    x = i;
                    y = j;
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }

        int ans = 0;

        //up
        for (int i = x - 1; i >= 0; --i) {
            if (board[i][y] == 'B') {
                break;
            } else if (board[i][y] == 'p') {
                ans++;
                break;
            }
        }

        //down
        for (int i = x + 1; i < board.size(); ++i) {
            if (board[i][y] == 'B') {
                break;
            } else if (board[i][y] == 'p') {
                ans++;
                break;
            }
        }

        //left
        for (int i = y - 1; i >= 0; --i) {
            if (board[x][i] == 'B') {
                break;
            } else if (board[x][i] == 'p') {
                ans++;
                break;
            }
        }

        //down
        for (int i = y + 1; i < board[0].size(); ++i) {
            if (board[x][i] == 'B') {
                break;
            } else if (board[x][i] == 'p') {
                ans++;
                break;
            }
        }

        return ans;
    }
};


int main() {
    return 0;
}
