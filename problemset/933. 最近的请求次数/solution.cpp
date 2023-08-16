#include <iostream>
#include <queue>
using namespace std;

class RecentCounter
{
    queue<int> que;

public:
    RecentCounter()
    {
    }

    int ping(int t)
    {
        que.push(t);
        // cout << que.front() << endl;
        while (que.front() < t - 3000)
        {
            que.pop();
        }
        return que.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */

int main()
{
    RecentCounter *obj = new RecentCounter();
    cout << obj->ping(1) << endl;
    cout << obj->ping(10) << endl;
    cout << obj->ping(3001) << endl;
    cout << obj->ping(3002) << endl;
    return 0;
}