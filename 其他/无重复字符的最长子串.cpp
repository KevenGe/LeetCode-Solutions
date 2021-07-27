class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        map<char, int> maps;

        int a = 0;
        int b = 0;

        int ans = 0;

        for (int i = 0; i < s.length(); ++i)
        {
            b = i;
            if (maps.find(s[i]) != maps.end())
            {
                if (maps[s[i]] >= a)
                {
                    a = maps[s[i]] + 1;
                }
                maps[s[i]] = i;
            }
            else
            {
                maps.insert(map<char, int>::value_type(s[i], i));
            }

            if (b - a + 1 > ans)
                ans = b - a + 1;
        }
        return ans;
    }
};