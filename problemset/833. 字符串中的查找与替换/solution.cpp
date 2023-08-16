#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
  public:
    string findReplaceString(string s, vector<int> &indices, vector<string> &sources, vector<string> &targets)
    {
        string ans = "";
        vector<int> idxs(indices.size(), 0);
        for (int i = 0; i < indices.size(); i++)
        {
            idxs[i] = i;
        }
        sort(idxs.begin(), idxs.end(), [&](int a, int b) { return indices[a] < indices[b]; });

        int sidx = 0;
        int iidx = 0;
        while (sidx < s.size())
        {
            if (iidx < idxs.size())
            {
                bool findGoodOne = false;
                while (iidx < idxs.size() && indices[idxs[iidx]] == sidx)
                {
                    if (s.substr(indices[idxs[iidx]], sources[idxs[iidx]].size()) == sources[idxs[iidx]])
                    {
                        findGoodOne = true;
                        ans += targets[idxs[iidx]];
                        sidx += sources[idxs[iidx]].size();
                        iidx += 1;
                        break;
                    }
                    iidx += 1;
                }
                if (!findGoodOne)
                {
                    ans += s[sidx];
                    sidx += 1;
                }
            }
            else
            {
                ans += s[sidx];
                sidx += 1;
            }
        }

        return ans;
    }
};

int main()
{
    Solution so;
    vector<int> indices = {3, 5, 1};
    vector<string> sources = {"kg", "ggq", "mo"};
    vector<string> targets = {"s", "so", "bfr"};

    cout << so.findReplaceString("vmokgggqzp", indices, sources, targets) << endl;
    return 0;
}
