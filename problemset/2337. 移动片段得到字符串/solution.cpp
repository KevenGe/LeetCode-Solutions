#include <iostream>
#include <string>

using namespace std;

class Solution
{
  public:
    bool canChange(string start, string target)
    {
        if (start.length() != target.size())
        {
            return false;
        }

        {
            int startIdx = 0;
            int targetIdx = 0;

            while (startIdx < start.size() && targetIdx < target.size())
            {
                while (startIdx < start.size() && start[startIdx] == '_')
                {
                    startIdx += 1;
                }

                while (targetIdx < target.size() && target[targetIdx] == '_')
                {
                    targetIdx += 1;
                }

                
                if ((start[startIdx] != target[targetIdx]) || (start[startIdx] == 'L' && startIdx < targetIdx) ||
                    (start[startIdx] == 'R' && startIdx > targetIdx))
                {
                    return false;
                }

                startIdx += 1;
                targetIdx += 1;
            }

            while (startIdx < start.size() && start[startIdx] == '_')
            {
                startIdx += 1;
            }

            while (targetIdx < target.size() && target[targetIdx] == '_')
            {
                targetIdx += 1;
            }

            if (startIdx != targetIdx)
            {
                return false;
            }
        }

        return true;
    }
};
