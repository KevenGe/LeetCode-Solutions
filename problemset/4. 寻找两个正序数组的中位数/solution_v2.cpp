#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        // start index of the list
        int l1s = 0;
        int l2s = 0;

        // end index of the list
        int l1e = nums1.size() - 1;
        int l2e = nums2.size() - 1;

        // mainloop
        int k = (nums1.size() + nums2.size());
        while (k != 1)
        {
            int k2 = k / 2;
            if (l1s + k2 <= l1e && l2s + k2 <= l2e)
            {
                l1s = l1s + k2;
                l2s = l2s + k2;
            }
            else if (l1s + k2 > l1e)
            {
                k2 = k - (l1e - l1s + 1);
                l1s = l1e + 1;
                l2s += k2;
            }
        }
    }
};

int main()
{
    return 0;
}