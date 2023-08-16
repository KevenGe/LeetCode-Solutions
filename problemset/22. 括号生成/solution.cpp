#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;

class Solution
{
public:
    vector<string> ans;
    vector<string> generateParenthesis(int n)
    {
        gen(n, 0, "");
        return ans;
    }
    void gen(int last_l, int last_r, string tmp)
    {
        if (last_l > 0)
        {
            gen(last_l - 1, last_r + 1, tmp + "(");

            if (last_r > 0)
            {
                gen(last_l, last_r - 1, tmp + ")");
            }
        }
        else if (last_r > 0)
        {
            gen(last_l, last_r - 1, tmp + ")");
        }
        else
        {
            ans.push_back(tmp);
        }
    }
};

int main()
{
    return 0;
}