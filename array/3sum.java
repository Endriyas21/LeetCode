class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums); // Sort the array to use two-pointer technique

        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate elements
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int curr = nums[i];
            int l = i + 1;
            int r = nums.length - 1;

            while (l < r) {
                int curr_sum = curr + nums[l] + nums[r];

                if (curr_sum == 0) {
                    res.add(Arrays.asList(curr, nums[l], nums[r]));
                    l++;
                    r--;

                    // Skip duplicate elements
                    while (l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
                } else if (curr_sum < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }

        return res;
    }
}