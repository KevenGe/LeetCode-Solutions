#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int sum[4] = {0};
    int current = 0;
    int i = 1;
    while (true)
    {
        if(i%7 == 0)
        {
            sum[current]++;
        }
        i++;
        current = (current+1)%4;
    }
    for(int x:sum)
    {
        cout << x << endl;
    }
    return 0;
}