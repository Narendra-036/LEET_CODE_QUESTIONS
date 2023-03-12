class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int s=accumulate(nums.begin(),nums.end(),0);
        int ls=0;
        for(int i=0; i<nums.size(); i++){
            if (ls==(s-ls-nums[i])){
                // cout<<ls;
                return i;
            }
        
            ls=ls+nums[i];
        }
        return -1;
        
    }
};