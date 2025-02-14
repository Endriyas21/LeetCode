class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        Arrays.fill(prefix, 1);

        int[] post = new int[nums.length];
        Arrays.fill(post, 1);

        for (int i=1; i < nums.length; i++){
            prefix[i] = nums[i-1] * prefix[i-1]; 
        }

        for (int i = nums.length-2; i >=0; i--){
            post[i] = nums[i+1] * post[i+1];
        }

        int[] store = new int[nums.length];
        for (int i=0; i < nums.length; i++){
            store[i] = prefix[i] * post[i];
        }
        return store;

    }
}