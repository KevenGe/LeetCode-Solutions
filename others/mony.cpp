/**
 * 长亭 D 题目
 * 申请经费
 *
 * 【已解决】
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<vector<int>> m(N + 1, vector<int>(N + 1, INT_MAX));
        for (int i = 0; i <= N; i++) {
            m[i][i] = 0;
        }
        vector<bool> used(N + 1, false);
        vector<int> minCost(N + 1, INT_MAX);

        int t;
        for (int i = 0; i < N; i++) {
            cin >> t;
            m[0][i + 1] = t;
            m[i + 1][0] = t;
        }

        int a, b, c;
        for (int i = 0; i < M; i++) {
            cin >> a >> b >> c;
            m[a][b] = min(m[a][b], c);
            m[b][a] = m[a][b];
        }

//        最小生成树算法
        int res = 0;
        used[0] = true;
        for (int i = 0; i <= N; i++) {
            minCost[i] = m[0][i];
        }

        while (true) {
            int choose_i = -1;
            for (int i = 0; i <= N; i++) {
                if (!used[i] && (choose_i == -1 || minCost[choose_i] > minCost[i])) {
                    choose_i = i;
                }
            }

            if (choose_i == -1) {
                break;
            }

            used[choose_i] = true;
            res += minCost[choose_i];

            for (int i = 0; i <= N; i++) {
                minCost[i] = min(minCost[i], m[choose_i][i]);
            }
        }
        cout << res << endl;
    }
    return 0;
}