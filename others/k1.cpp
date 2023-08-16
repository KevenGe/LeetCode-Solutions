#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()

{
    bool dp[1001][1001];
    int n, m;
    cin >> n m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dp[i][j] = false;
        }
    }

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        dp[a][b] = true;
    }

    for (int i = 0; i < n; i++)
    {
        int count = 0;
        for (int j = 0; j < n; j++)
        {
            if (dp[j][i] == true)
            {
                count += 1;
            }
        }

        for (int j = 0; j < n; j++)
        {
            if (dp[i][j] == true)
            {
                count -= 1;
            }
        }
        cout << count << endl;
    }

    return 0;
}