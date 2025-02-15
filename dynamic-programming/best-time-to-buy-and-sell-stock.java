class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int maxProfit = 0;
        for (int r = 0; r < prices.length; r++) {
            if (prices[l] > prices[r]) {
                l = r;
            }
            maxProfit = Math.max(maxProfit, prices[r] - prices[l]);
        }
        return maxProfit;
    }
}