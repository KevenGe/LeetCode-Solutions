/*
 * 长亭 面试题 C题
 *
 *
 * 题目
 * C 公司安全团队为了提升企业网络安全防护能力，会经常组织网络安全攻防演练，在一次演练中，Alice 作为攻方选手，成功获取了某台内网主机的权限。不过防守方也提前做了很多准备，为网络中的各台主机配置了复杂的拓扑关系，但是这些信息已经被机智的 Alice 通过物理渗透获取到了。Alice 发现，她攻击的内网中有 N 台主机，其中只有部分机器能够互通，并且攻击方需要窃取的目标信息被分别放在了其中 K 台主机上。为了尽可能避免被防守方发现，Alice 需要让自己攻击过程中在主机之间跳转的次数尽可能少，请你帮她分析最优的攻击路径至少需要多少次主机之间的跳转。

PS: Alice 作为一名经验丰富的白帽子，只要两台主机互相连通，她便可以从其中一台跳转到另一台。

PPS:需要注意的是，由于特殊的网络配置，从主机 a 跳转到主机 b，再从 b 跳转到 a，这是两次跳转行为。不要理解为从 a 机器 ssh 到 b 机器，然后从 b 机器上Ctrl ^D


 */

#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <climits>

using namespace std;

const int MAX_V = 505;      // 最大的节点数

vector<int> G[MAX_V];          // 邻接表

vector<vector<int>> d(MAX_V, vector<int>(MAX_V, INT_MAX / 10));  // 节点与节点之间的二维矩阵

/**
 * 给两个s,t节点添加双向的边，默认距离为1
 *
 * @param s 起点
 * @param t 终点
 */
void add_edge(int s, int t) {
    G[s].push_back(t);
    G[t].push_back(s);
    d[s][t] = 1;
    d[t][s] = 1;
}

/**
 * 【调试使用】展示距离d
 */
void showD() {
    cout << endl;
    for (int i = 1; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            cout << d[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    cout << endl;
}

int N, K;// N 台主机，K个目标
int tars[11];   // 目标主机的下标
bool used[11];  // 主机是否已访问

/**
 * 深度优先搜索
 * 只搜索目标主机，通过给出的节点在tars的下标来获取遍历全部目标主机的最小路径距离。
 *
 * @param i 起始节点在tars中的下标
 * @return
 */
int dfs(int i) {
    used[i] = true;
    int ans = INT_MAX / 10;
    for (int j = 1; j <= K; j++) {
        if (!used[j] && d[tars[i]][tars[j]] != INT_MAX / 10) {
            int t = dfs(j);
            if (t == INT_MAX / 10) {
                continue;
            }
            ans = min(ans, d[tars[i]][tars[j]] + t);
        }
    }
    if (ans == INT_MAX / 10) {
        for (int j = 1; j <= K; j++) {
            if (!used[j]) {
                used[i] = false;
                return INT_MAX / 10;
            }
        }
        used[i] = false;
        return 0;
    }
    used[i] = false;
    return ans;
}


/**
 * 主函数
 *
 * @return
 */
int main() {
    int T;
    cin >> T;
    while (T--) {

        // 输入N 台主机，K个目标
        cin >> N >> K;

        // 初始化d
        for (int i = 1; i <= N; i++) {
            fill(d[i].begin(), d[i].end(), INT_MAX / 10);
            d[i][i] = 0;
        }

        // 初始化used
        fill(used, used + 11, false);

        // 输入目标主机
        for (int i = 1; i <= K; i++) {
            cin >> tars[i];
        }

        // 输入边
        int M;
        cin >> M;
        int a, b;
        for (int i = 0; i < M; i++) {
            cin >> a >> b;
            add_edge(a, b);
        }
//        showD();
        // 佛洛依德算法
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    d[i][j] = min(d[i][k] + d[k][j], d[i][j]);
                }
            }
        }
//        showD();

        // 深搜遍历
        int ans = INT_MAX / 10;
        for (int i = 1; i <= K; i++) {
            int t2 = dfs(i);
            int t = d[1][tars[i]] + dfs(i);
            if (t < ans) {
                ans = t;
            };
        }
        if (ans == INT_MAX / 10) {
            cout << -1 << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}