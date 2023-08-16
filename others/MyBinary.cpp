#include <iostream>

using namespace std;

bool findit(int a[], int left, int right, int target)
{
    bool is_find = false;
    while (left <= right)
    {
        int middle = (left + right) / 2;
        if (a[middle] > target)
        {
            right = middle - 1;
        }
        else if (a[middle] < target)
        {
            left = middle + 1;
        }
        else
        {
            is_find = true;
            break;
        }
    }
    return is_find;
}

bool findit_by_digui(int a[], int left, int right, int target)
{
    if(left <= right)
    {
        int middle = (left + right)/2;
        if(a[middle] < target)
        {
            return findit_by_digui(a, middle+1, right, target);
        }else if (a[middle] > target)
        {
            return findit_by_digui(a, left, middle-1, target);
        }
        else
        {
            return true;
        }
        
        
    }
    return false;
}

int main()
{
    int a[] = {1, 3, 5, 6, 7};
    for (int i=0;i<10;++i)
    {
        cout << findit_by_digui(a, 0, 4, i) << endl;
    }
    return 0;
}