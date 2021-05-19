/**
 * @brief 归并排序
 * @author Keven Ge
 * @date 2020-07-02
 */

#include <iostream>
#include <vector>

using namespace std;

void mergeSort(vector<int> &arr, int left, int right)
{
    if (left == right)
    {
        return;
    }

    int mid = (left + right) / 2;
    int ll = left;
    int lr = mid;
    int rl = mid + 1;
    int rr = right;

    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);

    vector<int> reg(right - left + 1, 0);
    int k = 0;
    while (ll <= lr && rl <= rr)
    {
        cout << k << " " << ll << " " << rl << endl;
        reg[k++] = arr[ll] < arr[rl] ? arr[ll++] : arr[rl++];
    }

    while (ll <= lr)
    {
        reg[k++] = arr[ll++];
    }

    while (rl <= rr)
    {
        reg[k++] = arr[rl++];
    }

    for (int i = left; i <= right; i++)
    {
        arr[i] = reg[i - left];
    }
}

int main()
{
    vector<int> res;
    res.push_back(1);
    res.push_back(3);
    res.push_back(2);
    res.push_back(4);
    res.push_back(6);
    res.push_back(5);
    res.push_back(19);
    res.push_back(32);
    res.push_back(1);
    res.push_back(34);

    mergeSort(res, 0, 9);
    for (auto x : res)
    {
        cout << x << endl;
    }
    return 0;
}
