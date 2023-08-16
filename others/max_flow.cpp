//
// Created by lenovo on 2020-10-15.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

const int MAX_V = 50;   // 最大的节点数

// 边结构
struct edge {
    int to;         // 指向的边
    int cap;        // 剩余容量
    int rev;        // 相反的边

    edge(int to_, int cap_, int rev_) : to(to_), cap(cap_), rev(rev_) {}
};

vector<edge> G[MAX_V];      // 顶点
bool used[MAX_V];           // 是否已经使用过

// 新增一条表
void add_edge(int from, int to, int cap) {
    G[from].emplace_back(to, cap, G[to].size());
    G[to].emplace_back(from, 0, G[from].size() - 1);
}

// 通过dfs找到应该的路
int dfs(int v, int t, int f) {
    if (v == t) {
        return f;
    }

    used[v] = true;

    for (int i = 0; i < G[v].size(); i++) {
        edge &e = G[v][i];
        if (!used[e.to] && e.cap > 0) {
            int d = dfs(e.to, t, min(f, e.cap));
            if (d > 0) {
                e.cap -= d;
                G[e.to][e.rev].cap += d;
                return d;
            }
        }
    }
    return 0;
}

// 最大流算法
int max_flow(int s, int t) {
    int flow = 0;
    while (true) {
        fill(used, used + MAX_V, false);
        int d = dfs(s, t, INT_MAX);
        if (d == 0) {
            return flow;
        }
        flow += d;
    }
    return 0;
}

int main() {
    // T
    int T;
    cin >> T;
    while(T--){
        // 输入NK
        int N, K;
        cin >> N >> K;

        vector<int> cans(N + K + 2, 0);
        // 输入客户对能力的需求
        for (int i = 0; i < N; i++) {
            cin >> cans[i];
        }

        // 输入技术支持的能力
        for (int i = N; i < N + K; i++) {
            cin >> cans[i];
        }

        int s = N + K;        // 起点
        int t = N + K + 1;      // 终点

        // 清空边
        for(int i=0;i<MAX_V;i++){
            G[i].clear();
        }


        for (int i = 0; i < N; i++) {
            add_edge(s, i, 1);
        }
        for (int i = N; i < N + K; i++) {
            add_edge(i, t, 1);
        }
        for (int i = 0; i < N; i++) {
            for (int j = N; j < N + K; j++) {
                if (cans[i] <= cans[j]) {
                    add_edge(i, j, 1);
                }
            }
        }

        cout << max_flow(s, t) << endl;
    }
    return 0;
}