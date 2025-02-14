class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> store = new HashSet<>();
        for (int num: nums){
            store.add(num);
        }

        int res = 0;

        for (int n: nums){
            if(!store.contains(n-1)){
                int currentNum = n;
                int currLen = 1;

                while (store.contains(n+ 1)){
                    currLen++;
                    currentNum++;
                }
                res = Math.max(currLen, res); 

            }
        }
        return res;
        
    }
}