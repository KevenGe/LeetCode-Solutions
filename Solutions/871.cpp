#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>> &stations)
    {
        int ans = 0;
        int pos = 0;
        int tank = startFuel;
        priority_queue<int> pri;
        for (int i = 0; i < stations.size(); ++i)
        {
            int d = stations[i][0] - pos;

            while (tank - d < 0)
            {
                if (!pri.empty())
                {
                    tank += pri.top();
                    pri.pop();
                    ans++;
                }
                else
                {
                    return -1;
                }
            }
            tank -= d;
            pos += d;
            pri.push(stations[i][1]);
        }

        while (pos + tank < target && !pri.empty())
        {
            tank += pri.top();
            pri.pop();
            ans++;
        }

        if (pos + tank >= target)
        {
            return ans;
        }
        else
        {
            return -1;
        }
    }
};

int main()
{
    vector<vector<int>> vec;

    vector<int> vec_1;
    vec_1.push_back(10);
    vec_1.push_back(60);
    vec.push_back(vec_1);

    vector<int> vec_2;
    vec_2.push_back(20);
    vec_2.push_back(30);
    vec.push_back(vec_2);

    vector<int> vec_3;
    vec_3.push_back(30);
    vec_3.push_back(30);
    vec.push_back(vec_3);

    vector<int> vec_4;
    vec_4.push_back(60);
    vec_4.push_back(40);
    vec.push_back(vec_4);

    Solution so;
    cout <<so.minRefuelStops(100, 10, vec) << endl;
    return 0;
}