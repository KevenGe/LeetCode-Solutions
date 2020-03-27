class Solution
{
public:
    int hammingDistance(int x, int y)
    {
        int z = x ^ y;
        int c = 1;
        int ans = 0;
        for (int i = 0; i < 32; ++i)
        {
            if (c & z)
            {
                ans++;
            }
            c = c << 1;
        }
        return ans;
    }
};