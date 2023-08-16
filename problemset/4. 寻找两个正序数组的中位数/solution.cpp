/*
4. 寻找两个有序数组的中位数

@TIme : 2020-02-22 15:12
@auther: Keven Ge
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int m = nums1.size();
        int n = nums2.size();
        if (m <= n)
        {
            int i, j;

            int imin = 0;
            int imax = m;

            while (imin <= imax)
            {
                i = (imin + imax) / 2;
                j = (m + n + 1) / 2 - i;

                if (i != m && j != 0 && nums2[j - 1] >= nums1[i])
                {
                    imin = i + 1;
                }
                else if (i != 0 && j != n && nums1[i - 1] > nums2[j])
                {
                    imax = i - 1;
                }
                else
                {
                    if ((m + n) % 2 == 0)
                    {
                        double nums_min = 0, // 低的最大值
                            nums_max = 0;    // 高的最小值
                        if (i == 0)
                        {
                            nums_min = double(nums2[j - 1]);
                            if (i != m)
                            {
                                if (j != n)
                                {
                                    nums_max = min(double(nums1[0]), double(nums2[j]));
                                }
                                else
                                {
                                    nums_max = double(nums1[i]);
                                }
                            }
                            else
                            {
                                nums_max = double(nums2[j]);
                            }
                        }
                        else if (i == m)
                        {
                            if (j != 0)
                            {
                                nums_min = double(max(nums1[i - 1], nums2[j - 1]));
                            }
                            else
                            {
                                nums_min = nums1[i - 1];
                            }

                            nums_max = double(nums2[j]);
                        }
                        else
                        {
                            nums_min = double(max(nums1[i - 1], nums2[j - 1]));
                            nums_max = double(min(nums1[i], nums2[j]));
                        }
                        // cout << nums_min << endl;
                        // cout << nums_max << endl;
                        // cout << nums_max - nums_min << endl;
                        double sum = (nums_max - nums_min) / 2;
                        // cout << sum << endl;
                        sum = sum + nums_min;
                        // cout << sum << endl;

                        return sum;
                    }
                    else
                    {
                        double nums_min;
                        if (i)
                        {
                            nums_min = double(max(nums1[i - 1], nums2[j - 1]));
                        }
                        else
                        {
                            nums_min = double(nums2[j - 1]);
                        }
                        return nums_min;
                    }
                }
            }
        }
        else
        {
            return findMedianSortedArrays(nums2, nums1);
        }
        return -1;
    }
};

int main()
{
    vector<int> vec1, vec2;
    vec1.push_back(100001);
    //vec1.push_back(2);
    // vec2.push_back(1);
    vec2.push_back(100000);
    //vec2.push_back(3);

    Solution so;
    printf("%f\n", so.findMedianSortedArrays(vec1, vec2));
    //cout << 20001.5 << endl;
    //printf("%f", 20000001.5);
    return 0;
}