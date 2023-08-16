#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class MyStack
{
private:
    queue<int> queues;
    queue<int> queues_back;

public:
    /** Initialize your data structure here. */
    MyStack()
    {
        // Nothing
    }

    /** Push element x onto stack. */
    void push(int x)
    {
        queues.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop()
    {
        int res = 0;
        if (queues.empty())
        {
            res = -1;
        }
        else
        {
            for (int i = 1; i < queues.size(); ++i)
            {
                queues.push(queues.front());
                queues.pop();
            }
            res = queues.front();
            queues.pop();
        }
        return res;
    }

    /** Get the top element. */
    int top()
    {
        int res = 0;
        if (queues.empty())
        {
            res = -1;
        }
        else
        {
            for (int i = 1; i < queues.size(); ++i)
            {
                queues.push(queues.front());
                queues.pop();
            }
            res = queues.front();
            queues.push(queues.front());
            queues.pop();
        }
        return res;
    }

    /** Returns whether the stack is empty. */
    bool empty()
    {
        return queues.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

int main()
{
    MyStack m;
    m.push(1);
    m.push(2);
    cout << m.top() << endl;
    cout << m.pop() << endl;

    return 0;
}