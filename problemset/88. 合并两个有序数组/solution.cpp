#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int nums1Index = m - 1;
        int nums2Index = n - 1;

        for (int i = nums1.size() - 1; i >= 0; i--)
        {

            if (nums1Index >= 0 && (nums2Index < 0 || nums1[nums1Index] > nums2[nums2Index]))
            {
                nums1[i] = nums1[nums1Index];
                nums1Index -= 1;
            }
            else
            {
                nums1[i] = nums2[nums2Index];
                nums2Index -= 1;
            }
        }
    }
};

int main()
{
    return 0;
}