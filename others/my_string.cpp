#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a = "123456789101112131415";
    cout << a << "\'s substring is " << a.substr(2, 2) << endl;
    // for (string::iterator iter = a.begin(); iter != a.end(); iter++)
    // {
    //     cout << *iter << endl;
    // }

    // cout << *a.end() << endl;
    cout <<a.npos<<endl;
    cout << a.find("223123", 1) << endl;
    cout << a.replace(1, 2, "1111111") << endl;
    cout << a.replace(1, 2, 4, 'a') << endl;
    return 0;
}