#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int max_area = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right)
        {
            if (height[left] < height[right])
            {
                max_area = max(max_area, (right - left) * (height[left]));
                left++;
            }else
            {
                max_area = max(max_area, (right - left) * (height[right]));
                right--;
            }
            
        }
        return max_area;
    }
};

int main()
{
    return 0;
}