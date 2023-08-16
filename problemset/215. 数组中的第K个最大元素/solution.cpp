#include<iostream>
#include <vector>

using namespace std;

int getPivot(vector<int> &arr, int startIndex, int endIndex) {
    int left = startIndex;
    int pivot = arr[left];
    int pivotIndex = left;
    int right = endIndex;

    while (left != right) {
        // right to left
        while (left < right && arr[right] >= pivot) {
            right--;
        }

        // left to right
        while (left < right && arr[left] <= pivot) {
            left++;
        }

        if (left < right) {
            int t = arr[left];
            arr[left] = arr[right];
            arr[right] = t;
        }
    }

    int tmp = arr[left];
    arr[left] = pivot;
    arr[pivotIndex] = tmp;
    return left;
}

void quickSort(vector<int> &arr, int left, int right) {
    if (left >= right) {
        return;
    }

    int le = getPivot(arr, left, right);

    quickSort(arr, left, le - 1);
    quickSort(arr, le + 1, right);
}


class Solution {
public:
    int findKthLargest(vector<int> &nums, int k) {
        int left = 0;
        int right = nums.size() - 1;
        k = nums.size() - k;

        int ans = findIndex(nums, left, right);
        while (ans != k) {
            if (ans > k) {
                ans = findIndex(nums, left, ans - 1);
            } else {
//                k = k - ans - 1;
                ans = findIndex(nums, ans + 1, right);
            }
        }

        return nums[ans];
    }

    int findIndex(vector<int> &nums, int left, int right) {
        int p = nums[left];
        int pi = left;

        while (left != right) {
            while (left < right && nums[right] >= p) {
                right--;
            }

            while (left < right && nums[left] <= p) {
                left++;
            }

            if (left < right) {
                int t = nums[left];
                nums[left] = nums[right];
                nums[right] = t;
            }
        }

        int t = nums[left];
        nums[left] = p;
        nums[pi] = t;

        return left;
    }
};

int main() {
    vector<int> arr;
    arr.push_back(3);
    arr.push_back(2);
    arr.push_back(1);
    arr.push_back(5);
    arr.push_back(6);
    arr.push_back(4);

    Solution so;
    cout << so.findKthLargest(arr, 2) << endl;

    for (int i : arr) {
        cout << i << endl;
    }

    return EXIT_SUCCESS;
}