#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int longestPalindrome(string s)
    {
        unordered_map<char, int> count;
        for (char ch : s)
        {
            count[ch]++;
        }
        int ans = 0;
        for (auto pp : count)
        {
            ans += pp.second / 2 * 2;
            if (pp.second % 2 == 1 && ans % 2 == 0)
            {
                ans += 1;
            }
        }
        return ans;
    }
};

int main()
{
    return 0;
}