class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> ans;
        map<int, int> maps;
        for (unsigned i = 0; i < nums.size(); ++i)
        {
            if (maps.find(target - nums[i]) != maps.end())
            {

                ans.push_back(maps[target - nums[0]]);
                ans.push_back(i);
                return ans;
            }
            else
            {
                maps.insert(map<int, int>::value_type(nums[i], i));
            }
        }
        return ans;
    }
};
