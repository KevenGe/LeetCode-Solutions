#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <climits>

using namespace std;

const int MAX_V = 505;


typedef pair<int, int> P;

vector<int> G[MAX_V];
int d[MAX_V];


void djs(int s) {
    priority_queue<P, vector<P>, greater<>> que;
    fill(d, d + MAX_V, INT_MAX);
    d[s] = 0;
    que.push(P(0, s));

    while (!que.empty()) {
        P p = que.top();
        que.pop();
        int v = p.second;
        if (d[v] < p.first) {
            continue;
        }

        for (int j = 0; j < G[v].size(); j++) {
            int e = G[v][j];
            if (d[e] > d[v] + 1) {
                d[e] = d[v] + 1;
                que.push(P(d[e], e));
            }
        }
    }
}

void add_edge(int s, int t) {
    G[s].push_back(t);
    G[t].push_back(s);
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, K;
        cin >> N >> K;
        vector<int> tars(K);
        for (int i = 0; i < K; i++) {
            cin >> tars[i];
        }

        int M;
        cin >> M;
        int a, b;
        for(int i=0;i< M; i++){
            cin >> a >> b;
            add_edge(a, b);
        }
    }
    return 0;
}