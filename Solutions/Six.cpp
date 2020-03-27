#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

int INF = 2000000000;
const int max_n = 302;
const int max_m = 10001;
int d[max_n][max_n];
int a[max_m];

int main()
{
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            d[i][j] = INF;
        }
    }
    for (int i = 0; i < N; ++i)
    {
        d[i][i] = 0;
    }

    while (M--)
    {
        int m_num;
        cin >> m_num;
        for (int i = 0; i < m_num; ++i)
        {
            cin >> a[i];
        }
        for (int i = 0; i < m_num; ++i)
        {
            for (int j = 1; j < m_num; ++j)
            {
                if (i != j)
                {

                    d[a[i] - 1][a[j] - 1] = 1;
                    d[a[j] - 1][a[i] - 1] = 1;
                }
            }
        }
    }

    for (int k = 0; k < N; ++k)
    {
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    int ans = INF;
    for (int i = 0; i < N; ++i)
    {
        int tmp = 0;
        for (int j = 0; j < N; ++j)
        {
            tmp += d[i][j];
        }
        ans = min(ans, tmp);
    }

    printf("%d\n", (ans / (N - 1)) * 100);
    return 0;
}