#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


// leetcode 289

class Solution {
public:
    void gameOfLife(vector<vector<int>> &board) {
        vector<vector<int>> board_copy(board);
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {

                int num = 0;
                if (i - 1 >= 0) {
                    num += board[i - 1][j];
                    if (j - 1 >= 0) {

                        num += board[i - 1][j - 1];
                    }
                }
                if (j - 1 >= 0) {
                    num += board[i][j - 1];
                    if (i + 1 < board.size()) {
                        num += board[i + 1][j - 1];
                    }
                }
                if (i + 1 < board.size()) {
                    num += board[i + 1][j];
                    if (j + 1 < board[0].size()) {
                        num += board[i + 1][j + 1];
                    }
                }
                if (j + 1 < board[0].size()) {
                    num += board[i][j + 1];
                    if (i - 1 >= 0) {
                        num += board[i - 1][j + 1];
                    }
                }

                if (board[i][j] == 1) {
                    if (num < 2 || num > 3) {
                        board_copy[i][j] = 0;
                    }
                } else {
                    if (num == 3) {
                        board_copy[i][j] = 1;
                    }
                }
            }
        }

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                board[i][j] = board_copy[i][j];
            }
        }
    }
};


int main() {
    return 0;
}
