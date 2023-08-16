#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool cmp2(const string &as, const string &bs, const int i = 0)
{
    if (as.length() <= i)
    {
        if (bs[i] == bs[0])
        {
            return cmp2(bs.substr(1), bs.substr(i + 1) + as);
        }
        else
        {
            return bs[i] < bs[0];
        }
    }

    if (bs.length() <= i)
    {

        if (as[i] == as[0])
        {
            return cmp2(as.substr(i + 1) + bs, as.substr(1));
        }
        else
        {
            return as[i] > as[0];
        }
    }

    if (as[i] == bs[i])
    {
        return cmp2(as, bs, i + 1);
    }
    else
    {
        return as[i] > bs[i];
    }
};

bool cmp(int a, int b)
{
    const string as = to_string(a);
    const string bs = to_string(b);
    return cmp2(as, bs);
}

class Solution
{
public:
    string largestNumber(vector<int> &nums)
    {
        sort(nums.begin(), nums.end(), cmp);
        string ans = "";
        for (int x : nums)
        {
            ans += to_string(x);
        }

        if (ans[0] == '0')
        {
            return "0";
        }
        else
        {
            return ans;
        }
    }
};

int main()
{
    Solution so;
    vector<int> vec;
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    cout << so.largestNumber(vec) << endl;

    return 0;
}