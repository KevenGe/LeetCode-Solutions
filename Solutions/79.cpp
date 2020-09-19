/**
 * @file 79.cpp
 * @author your name (you@domain.com)
 * @brief
 * @version 0.1
 * @date 2020-08-13
 *
 * @copyright Copyright (c) 2020
 *
 */

#include <iostream>
#include <vector>

using namespace std;

/**
 * @brief
 *
 */
class Solution {
public:
    /**
     * @brief
     *
     * @param board
     * @param word
     * @return true
     * @return false
     */
    bool exist(vector<vector<char>> &board, string word) {
        if (board.empty() || word.length() == 0) {
            return false;
        }
        vector<vector<bool> > history(board.size(), vector<bool>(board[0].size(), false));

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, history, word, i, j)) {
                        return true;
                    };
                }
            }
        }
        return false;
    }

    bool dfs(const vector<vector<char> > &board, vector<vector<bool> > &history, string word, int i, int j) {
        if (word.length() == 0) {
            return true;
        } else if (i >= 0 && i < board.size() && j >= 0 && j < board[0].size()) {
            if (!history[i][j] && board[i][j] == word[0]) {
                history[i][j] = true;
                bool t =  dfs(board, history, word.substr(1), i - 1, j) ||
                       dfs(board, history, word.substr(1), i, j - 1) ||
                       dfs(board, history, word.substr(1), i + 1, j) ||
                       dfs(board, history, word.substr(1), i, j + 1);
                history[i][j] = false;
                return t;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
};

int main() {
    vector<vector<char> > board;

    vector<char> tmp;
    tmp.push_back('C');
    tmp.push_back('A');
    tmp.push_back('A');
    board.push_back(tmp);

    vector<char> tmp1;
    tmp1.push_back('A');
    tmp1.push_back('A');
    tmp1.push_back('A');
    board.push_back(tmp1);

    vector<char> tmp2;
    tmp2.push_back('B');
    tmp2.push_back('C');
    tmp2.push_back('D');
    board.push_back(tmp2);

    Solution so;
    cout << so.exist(board, "AAB") << endl;

    return 0;
}