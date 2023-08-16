class Solution
{
public:
    int getSum(int a, int b)
    {
        while(b != 0)
        {
            int c = a ^ b;
            int d = unsigned(a & b) << 1;
            a = c;
            b = d;
        }
        return a;
    }
};