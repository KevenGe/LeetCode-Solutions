//
// Created by lenovo on 2020-10-16.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <climits>

using namespace std;

const int MAX_TIME = 10000009;
const int MAX_N = 1000009;

int costs[MAX_N];
int used[MAX_N];
vector<int> G[MAX_N];

int N; // 数量
int P; // 阈值

int main() {
    int T;
    cin >> T;
    while (T--) {
        cin >> N >> P;

        for (int i = 1; i <= N; i++) {
            G[i].clear();
        }

        for (int i = 1; i <= N; i++) {
            cin >> costs[i];
        }

        int n, t;
        for (int i = 1; i <= N; i++) {
            cin >> n;
            while (n--) {
                cin >> t;
                G[i].push_back(t);
            }
        }

        // 算法
        if (P == 0) {
            cout << 0 << endl;
            continue;
        }

        fill(used + 1, used + N + 1, false);
        int num = 0;

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> que;
        que.emplace(costs[1], 1);

        int res = INT_MIN;

        while (!que.empty()) {
            pair<int, int> p = que.top();
            que.pop();
            if (used[p.second] == true) {
                continue;
            }
            used[p.second] = true;

            res = max(res, p.first);

            num += 1;
            if (num * 100 >= N * P) {
                cout << res + 1 << endl;
                break;
            }

            for (int j = 0; j < G[p.second].size(); j++) {
                t = G[p.second][j];
                que.emplace(costs[t], t);
            }
        }

        if (num * 100 < N * P) {
            cout << -1 << endl;
        }
    }
    return 0;
}