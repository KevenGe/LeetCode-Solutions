/******************************************************************************
 * @brief LeetCode 378
 * @author KevenGe
 * @date 2020-07-03
 *****************************************************************************/


#include <iostream>
#include <vector>
#include <queue>

using namespace std;


/**
 * @brief 这里使用归并排序的方式解题
 */
class Solution {
public:
    int kthSmallest(vector<vector<int>> &matrix, int k) {
        struct point {
            int val;
            int x;
            int y;

            point(int val_, int x_, int y_) {
                this->val = val_;
                this->x = x_;
                this->y = y_;
            }

            bool operator > (const point & a) const {
                return this->val > a.val;
            }
        };

        priority_queue<point, vector<point>, greater<point>> que;

        // initiative
        int n = matrix.size();
        for (int i = 0; i < n; ++i) {
            que.push(point(matrix[i][0], i, 0));
        }

        int m = 0;
        while (!que.empty()) {
            point t = que.top();
            que.pop();

            m++;
            if (m == k) {
                return t.val;
            } else if(t.y+1 != matrix[0].size()){
                que.push(point(matrix[t.x][t.y+1], t.x, t.y+1));
            }
        }
        return 0;
    }
};

int main() {
    return 0;
}
