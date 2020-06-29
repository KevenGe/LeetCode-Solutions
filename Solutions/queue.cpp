#include <iostream>
#include <vector>
using namespace std;

/* 
    😂 😂 😂 😂 😂 
 */

class MyCircularQueue
{
private:
    // int *que = new int[100];
    int *que;
    int s = 0;
    int e = 0;
    int maxLength = 0;
    int curLength = 0;

public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k)
    {
        // int *que = new int[100];
        // int que[100];
        // int s = 0;
        // int e = 0;
        que = new int[k + 1];
        maxLength = k;
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value)
    {
        if (isFull() == false)
        {
            que[e] = value;
            e = (e + 1) % maxLength;
            curLength += 1;
            return true;
        }
        else
        {
            return false;
        }
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue()
    {
        if (isEmpty())
        {
            return false;
        }
        else
        {
            s = (s + 1) % maxLength;
            curLength -= 1;
            return true;
        }
    }

    /** Get the front item from the queue. */
    int Front()
    {
        if (!isEmpty())
        {
            return que[s];
        }
        else
        {
            return -1;
        }
    }

    /** Get the last item from the queue. */
    int Rear()
    {
        if (!isEmpty())
        {
            if (e == 0)
            {
                return que[maxLength - 1];
            }
            else
            {
                return que[e - 1];
            }
        }
        else
        {
            return -1;
        }
    }

    /** Checks whether the circular queue is empty or not. */
    bool isEmpty()
    {
        return curLength == 0;
    }

    /** Checks whether the circular queue is full or not. */
    bool isFull()
    {
        return curLength == maxLength;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */

int main()
{
    return 0;
}
