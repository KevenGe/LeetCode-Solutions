#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int findJudge(int N, vector<vector<int>> &trust)
    {
        int *dp_in = new int[N];
        int *dp_out = new int[N];
        fill(dp_in, dp_in+N,0);
        fill(dp_out, dp_out+N,0);

        for(int i=0;i<trust.size();++i)
        {
            dp_out[trust[i][0]-1]++;
            dp_in[trust[i][1]-1]++;
        }

        for(int i=0;i<N;++i)
        {
            if(dp_out[i] == 0 && dp_in[i] == N-1)
            {
                return i+1;
            }
        }
        return -1;
    }
};

int mian()
{
    return 0;
}