#include <iostream>
#include <vector>

using namespace std;

class Solution
{
  public:
    int maxDistToClosest(vector<int> &seats)
    {
        int ans = -1;

        // front
        int frontOneIdx = -1;
        for (int i = 0; i < seats.size(); i++)
        {
            if (seats[i] == 1)
            {
                frontOneIdx = i;
                ans = max(ans, frontOneIdx);
                break;
            }
        }

        // back
        int backOneIdx = -1;
        for (int i = seats.size() - 1; i >= 0; i--)
        {
            if (seats[i] == 1)
            {
                backOneIdx = i;
                ans = max(ans, int(seats.size()) - 1 - backOneIdx);
                break;
            }
        }

        int continueZeroCount = 0;
        for (int i = frontOneIdx; i <= backOneIdx; i++)
        {
            if (seats[i] == 0)
            {
                continueZeroCount += 1;
            }
            else
            {
                ans = max(ans, (continueZeroCount + 1 ) / 2);
                continueZeroCount = 0;
            }
        }

        return ans;
    }
};
