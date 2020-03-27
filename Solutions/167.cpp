#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        vector<int> res;
        int left = 0;
        int right = numbers.size() - 1;
        while (left <= right)
        {

            int middle = (left + right) / 2;
            if (middle != (numbers.size() - 1 - middle))
            {
                int rtarget = target - numbers[middle];
                int rleft = middle + 1;
                int rright = numbers.size() - 1;

                // ！ 标志
                // 0 Not find
                // 1 Find
                // 
                int flag = 0;
                while (rleft <= rright)
                {
                    int rmiddle = (rleft + right) / 2;
                    {
                        if (numbers[rmiddle] == rtarget)
                        {
                            flag = 1;
                            break;
                        }
                    }
                }
                if (flag)
                {
                    res.push_back(middle);
                    res.push_back(numbers.size() - 1 - middle);
                    break;
                }
            }
        }
        return res;
    }
};

int main()
{
    vector<int> vec;
    vec.push_back(2);
    vec.push_back(7);
    vec.push_back(11);
    vec.push_back(15);

    Solution so;
    vec = so.twoSum(vec, 9);
    for (int x : vec)
    {
        cout << x << endl;
    }
    return 0;
}