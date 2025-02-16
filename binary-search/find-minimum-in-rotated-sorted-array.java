class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length -1;
        int res = Integer.MAX_VALUE;
        while (l <= r){
            if (nums[l] < nums[r]){
                res = Math.min(res, nums[l]);
                break;
            }
            int mid = (l +r)/2;
            res = Math.min(nums[mid], res);
            if (nums[l] <= nums[mid]){
                l = mid +1;
            }else{
                r = mid -1;
            }

        }
        return res;
    }
}