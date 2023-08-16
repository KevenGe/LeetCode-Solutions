#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> distributeCandies(int candies, int num_people)
    {
        long index = 0;
        vector<int> res(num_people, 0);
        while (candies >= index + 1)
        {
            res[index % num_people] += index + 1;
            index++;
            candies -= index;
        }

        res[index % num_people] += candies;
        return res;
    }
};

int main()
{
    Solution so;
    so.distributeCandies(7,4);
    return 0;
}