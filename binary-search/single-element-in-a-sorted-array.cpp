class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;
        
        while(left<=right){
            int m = left+(right-left)/2;
            
            // Fix: Handle boundary conditions properly
            if((m == 0 || nums[m-1] != nums[m]) && 
               (m == nums.size()-1 || nums[m+1] != nums[m])) {
                return nums[m];
            }

            int border = (m-1>=0 && nums[m-1] == nums[m]) ? m-1 : m;
            if(border%2==0){
                left=m+1;
            }
            else{
                right=m-1;
            }
        }
        return -1;
    }
};