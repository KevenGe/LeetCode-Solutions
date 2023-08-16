#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        map<string, vector<string>> maps;
        for (string str : strs)
        {
            string str_tmp = str;
            sort(str_tmp.begin(), str_tmp.end());
            if (maps.find(str_tmp) != maps.end())
            {
                maps[str_tmp].push_back(str);
            }
            else
            {
                vector<string> vec_tmp;
                vec_tmp.push_back(str);
                maps.insert(map<string, vector<string>>::value_type(str_tmp, vec_tmp));
            }
        }

        vector<vector<string>> res;
        for (map<string, vector<string>>::iterator iter = maps.begin(); iter != maps.end(); iter++)
        {
            res.push_back(iter->second);
        }
        return res;
    }
};

int main()
{
    return 0;
}