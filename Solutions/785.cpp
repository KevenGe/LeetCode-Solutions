#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
    vector<int> status;
    vector<vector<int>> *graph;
    bool isBad = false;

public:
    bool isBipartite(vector<vector<int>> &graph)
    {
        this->graph = &graph;
        status.assign(graph.size(), 0);
        status[0] = 1;
        dfs(0);
        return !isBad;
    }
    void dfs(int i)
    {
        if (isBad)
        {
            return;
        }
        for (int j = 0; j < graph[i].size(); j++)
        {
            int tar = graph[i][j];
            if (status[j] == 0)
            {
                status[j] = -status[i];
                dfs(j);
            }
            else if (status[j] == status[i])
            {
                isBad = true;
                return;
            }
        }
    }
};

int main()
{
    return 0;
}