#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    // chong dir
    bool isRectangleOverlap(vector<int> &rec1, vector<int> &rec2)
    {
        if (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]))
        {
            if(min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]))
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{
    return 0;
}