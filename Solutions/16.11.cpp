#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution
{
public:
    vector<int> divingBoard(int shorter, int longer, int k)
    {
        vector<int> res;
        if (k)
        {
            set<int> before_res;
            int basic = shorter * k;
            int dis = longer - shorter;
            before_res.insert(basic);
            for (int i = 1; i <= k; ++i)
            {
                basic += dis;
                before_res.insert(basic);
            }
            for(int x:before_res)
            {
                res.push_back(x);
            }
        }
        return res;
    }
};

int main()
{
    return 0;
}