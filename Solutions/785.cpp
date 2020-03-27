#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    bool isBipartite(vector<vector<int>> &graph)
    {
        //int *dp = new int[graph.size()];
        int dp[5] = {0};
        for (int i = 0; i < graph.size(); ++i)
        {
            dp[i] = i;
        }
        int *rank = new int[graph.size()];
        fill(rank, rank + graph.size(), 1);

        for (int i = 0; i < graph.size(); ++i)
        {
            if (graph[i].size() == 0)
                continue;
            int basic = graph[i][0];
            for (int j = 1; j < graph[i].size(); ++j)
            {
                unionit(dp, rank, basic, graph[i][j]);
            }
        }

        unordered_set<int> sets;
        for (int i = 0; i < graph.size(); ++i)
        {
            sets.insert(find(dp, i));
        }

        return sets.size() >= 2;
    }

    int find(int dp[], int x)
    {
        if (dp[x] == x)
        {
            return x;
        }
        else
        {
            return dp[x] = find(dp, dp[x]);
        }
    }

    void unionit(int dp[], int rank[], int x, int y)
    {
        x = find(dp, x);
        y = find(dp, y);
        if (!same(dp, x, y))
        {
            if (rank[x] < rank[y])
            {
                dp[x] = y;
            }
            else
            {
                dp[y] = x;
                if (rank[x] == rank[y])
                {
                    rank[x]++;
                }
            }
        }
    }

    bool same(int dp[], int x, int y)
    {
        return find(dp, x) == find(dp, y);
    }
};

int main()
{
    vector<vector<int>> vec;

    vector<int> vec1;
    vec1.push_back(4);
    // vec1.push_back(1);

    vector<int> vec2;
    // vec2.push_back(0);
    // vec2.push_back(2);

    vector<int> vec3;
    //vec3.push_back(1);
    vec3.push_back(4);

    vector<int> vec4;
    vec4.push_back(4);
    // vec4.push_back(2);

    vector<int> vec5;
    vec5.push_back(0);
    vec5.push_back(2);
    vec5.push_back(3);

    vec.push_back(vec1);
    vec.push_back(vec2);
    vec.push_back(vec3);
    vec.push_back(vec4);
    vec.push_back(vec5);

    Solution so;
    cout << so.isBipartite(vec) << endl;
    return 0;
}