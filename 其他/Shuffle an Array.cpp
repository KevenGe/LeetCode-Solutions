class Solution {
public:

    vector<int> nums;

    Solution(vector<int>& nums) {
        this->nums = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        this->nums[0]=1;
        this->nums[1]=2;
        this->nums[2]=3;
        return this->nums;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        srand(time(0));
        for(int i=0;i<3;++i){
            bool used[]={false,false,false};
            int select  = 0;
            do{
                select  = rand()%3;
            }while(used[select] == true);

            used[select]=true;
            this->nums[i] = select;
        }
        return this->nums;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */