#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> st;
        for (unsigned i = 0; i < s.length(); ++i)
        {
            if (st.empty())
            {
                st.push(s[i]);
            }
            else
            {
                switch (st.top())
                {
                case '(':
                    if (s[i] != ')')
                        return false;
                    else
                        st.pop();
                    break;
                case '{':
                    if (s[i] != '}')
                        return false;
                    else
                        st.pop();
                    break;
                case '[':
                    if (s[i] != ']')
                        return false;
                    else
                        st.pop();
                    break;
                default:
                    st.push(s[i]);
                    break;
                }
            }
        }

        if (s.empty() == false)
            return false;

        return true;
    }
};