class Solution
{
public:
    vector<string> fizzBuzz(int n)
    {
        vector<string> res;
        for (int i = 1; i <= n; ++i)
        {
            res.push_bacK(to_string(i)));
        }

        for (int i = 3; i <= res; i = i + 3)
        {
            res[i-1] = "Fizz";
        }

        for (int i = 5; i <= res; i = i + 5)
        {
            if(res[i-1] == "Fizz")
            {
                res[i-1]="FizzBuzz";
            }else
            {
                res[i-1]="Buzz";
            }
            
        }
        return res;
    }
};