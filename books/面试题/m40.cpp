#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<int> getLeastNumbers(vector<int> &arr, int k)
    {
        sort(arr.begin(), arr.end());
        vector<int> res ;
        for(int i=0;i<k;++i)
        {
            res.push_back(arr[i]);
        }
        return res;
    }
};

int main()
{
    return 0;
}