#include <iostream>
using namespace std;

// int dp[9] = {3, 5, 8, 1, 2, 9, 4, 7, 6};

void mysort(int dp[], int start, int end, int tar)
{
    int tar_num = dp[tar];
    int start_ori = start;
    int end_ori = end;
    while (start <= end)
    {
        while (dp[start] <= tar_num && start < tar)
        {
            start++;
        }

        while (dp[end] > tar_num && end > start)
        {
            end--;
        }

        if (end > start)
        {
            int tmp = dp[start];
            dp[start] = dp[end];
            dp[end] = tmp;
        }
        else
        {
            dp[tar] = dp[start];
            dp[start] = tar_num;

            mysort(dp, start_ori, start - 2, start - 1);
            mysort(dp, end + 1, end_ori, end_ori + 1);
            break;
        }
    }
}

int main()
{
    int dp[9] = {3, 5, 8, 1, 2, 9, 4, 7, 6};
    mysort(dp, 0, 7, 8);
    for (int i = 0; i < 9; ++i)
    {
        cout << dp[i] << endl;
    }
    return 0;
}
