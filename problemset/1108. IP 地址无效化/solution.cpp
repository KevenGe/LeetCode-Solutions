#include <iostream>
#include <string>
#include <string.h>
using namespace std;

class Solution
{
public:
    string defangIPaddr(string address)
    {
        int offset = 0;
        int pos;
        while ((pos = address.find(".", offset)) != address.npos)
        {
            address.replace(pos, 1, "[.]");
            offset = pos + 2;
        }
        return address;
    }
};

int main()
{
    Solution so;
    string res("127.0.0.1");
    cout << so.defangIPaddr(res);
    return 0;
}