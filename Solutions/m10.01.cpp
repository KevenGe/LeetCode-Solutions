#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void merge(vector<int> &A, int m, vector<int> &B, int n)
    {
        int ab = m - 1;
        int bb = n - 1;
        int tail = m + n - 1;
        while (ab >= 0 || bb >= 0)
        {

            if (ab < 0)
            {
                while (bb >= 0)
                {
                    A[tail] = B[bb];
                    tail--;
                    bb--;
                }
            }

            if (bb < 0)
            {
                while (ab >= 0)
                {
                    A[tail] = A[ab];
                    tail--;
                    ab--;
                }
            }

            if ( ab >=0 && bb >=0 && A[ab] > B[bb])
            {
                A[tail] = A[ab];
                ab--;
                tail--;
            }
            else if(ab >=0 && bb >=0 && A[ab] <= B[bb])
            {
                A[tail] = B[bb];
                bb--;
                tail--;
            }
        }
    }
};

int main()
{
    return 0;
}
