/*
 * LeetCode 22
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> res;
//    int left_k = 0;
    int n = 0;

    vector<string> generateParenthesis(int n) {
//        this->left_k = 0;
        this->n = n;
        dfs("", 0, 0);
        return res;
    }

    void dfs(string str, int cur_n, int left_n) {
        if (cur_n < this->n) {
            dfs(str + "(", cur_n + 1, left_n + 1);
            if (left_n > 0) {
                dfs(str + ")", cur_n, left_n - 1);
            }
        } else if ( left_n >0){
            dfs(str+")", cur_n, left_n -1);
        } else{
            res.push_back(str);
        }
    }
};

int main() {
    return 0;
}