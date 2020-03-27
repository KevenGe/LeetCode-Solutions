#include <iostream>
#include <queue>
using namespace std;

class MaxQueue
{
    queue<int> q;
    deque<int> dq;

public:
    MaxQueue()
    {
    }

    int max_value()
    {
        if (dq.empty())
        {
            return -1;
        }
        else
        {
            return dq.front();
        }
    }

    void push_back(int value)
    {
        q.push(value);

        while (dq.empty() == false && dq.back() < value)
        {
            dq.pop_back();
        }
        dq.push_back(value);
    }

    int pop_front()
    {
        if (!q.empty())
        {
            if (q.front() == dq.front())
            {
                dq.pop_front();
            }
            int tmp = q.front();
            q.pop();
            return tmp;
        }
        return -1;
    }
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue* obj = new MaxQueue();
 * int param_1 = obj->max_value();
 * obj->push_back(value);
 * int param_3 = obj->pop_front();
 */

int main()
{
    return 0;
}