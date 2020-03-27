#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    bool canThreePartsEqualSum(vector<int> &A)
    {
        long long sum = 0;
        for (int x : A)
        {
            sum += x;
        }

        if (sum % 3 != 0)
        {
            return false;
        }

        long long ans = sum / 3;

        long long ans_tmp = 0;
        int correct_time = 0;
        for (int x : A)
        {
            ans_tmp += x;
            if (ans_tmp == ans)
            {
                ans_tmp = 0;
                correct_time++;
            }
        }

        if ((correct_time == 3 && ans_tmp == 0) || (correct_time >3 && ans == 0))
        {
            return true;
        }
        return false;
    }
};

int main()
{
    vector<int> vec;
    vec.push_back(3);
    vec.push_back(3);
    vec.push_back(6);
    vec.push_back(5);
    vec.push_back(-2);
    vec.push_back(2);
    vec.push_back(5);
    vec.push_back(1);
    vec.push_back(-9);
    vec.push_back(4);

    Solution so;
    cout << so.canThreePartsEqualSum(vec);
    return 0;
}