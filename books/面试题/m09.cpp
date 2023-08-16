//
// Created by lenovo on 2020/6/21.
//

/**
 * 剑指 Offer 09. 用两个栈实现队列
 * @author Keven Ge
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

class CQueue {
private:
    stack<int> s1;
    stack<int> s2;
public:
    CQueue() {

    }

    void appendTail(int value) {
        s1.push(value);
    }

    int deleteHead() {
        if (s1.size() == 0){
            return -1;
        }

        while(s1.empty()!= true){
            s2.push(s1.top());
            s1.pop();
        }

        int ans = s2.top();
        s2.pop();

        while(s2.empty()!= true){
            s1.push(s2.top());
            s2.pop();
        }

        return ans;
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */

int main(){
    return 0;
}